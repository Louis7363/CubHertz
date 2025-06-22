#Projet : CubHertz
#Auteurs : Louis Colbert, Luc Vallet

import datetime
import queue
import wave
import numpy as np
import pyaudio
from ursina import *

from modules import calculRGB,spatial
from modules.Fourrier import fourrier
from modules.calculPosition import calcul_position


class Audio :
    """Class Audio ayant comme méthode : enregistrement_audio qui permet d'enregister un audio"""
    def __init__(self):
        self.format = pyaudio.paInt16 #format sur 16 bits
        self.channels = 1 #nombre de canaux d'entrées
        self.rate = 10000 # Spécifie le taux souhaité en Hz, 44 100 échantillons sont capturés chaque seconde
        self.chunk = 1000 #nombre d'échantillons correspondant à un bloc
        self.stream = None # attribut permettant de récuperer l'enregistrement brut
        self.audio = pyaudio.PyAudio() # carotte (un peu comme un micro)
        self.frames = [] # attribut contenant le fichier wav qui sera enregistré
        self.recording = False  # drapeau indiquant si l'enregistrement est en cours
        self.count = 0
        self.q = queue.Queue()
        self.r = 0
        self.g = 0
        self.b = 0


    # fonction pour arreter l'enregistrement
    def commencer_enregistrement(self) :

        self.stream = self.audio.open(format=self.format, channels=self.channels,
                        rate=self.rate, input=True,
                        frames_per_buffer=self.chunk,
                        stream_callback=self.ecrire_arriere_plan)

        print("Enregistrement en cours...")

        self.stream.start_stream() # Debut enregistrement
        self.recording = True # on active le drapeau : "l'audio est en cours".


    # fonction pour arreter l'enregistrement
    def arreter_enregistrement(self) :

        self.recording = False # on désactive le drapeau

        # on s'assure que le stream est bien ouvert avant vde le fermer
        if self.stream :
            # on ferme tout

            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
            self.audio.terminate()

    def ecrire_arriere_plan(self, audio_entrant, nb_echantillons, time_info, status):
        self.frames.append(audio_entrant)
        audio_concatenated = b''.join(self.frames)  # concatène toutes les frames

        # Conversion des données binaires en tableau NumPy de type int16
        audio_array = np.frombuffer(audio_concatenated, dtype=np.int16)
        self.frames = []
        if len(audio_array) >= 1000:
            frequenceFondamentale, frequenceHarmonique = fourrier(audio_array)
            print(f"FrequenceFondamentale : {frequenceFondamentale}, FrequenceHarmonique : {frequenceHarmonique}")
            r,g,b = calculRGB.rgb(max(audio_array))
            self.r,self.g,self.b = r,g,b
            self.q.put((frequenceFondamentale,frequenceHarmonique))
            audio_array = []


        if self.recording :
            flag = pyaudio.paContinue
        else :
            flag = pyaudio.paComplete
        return None, flag

    def creer_oeuvre(self) :
        print("creerOeuvreTest")

        global precedenteFrequenceFondamentale, precedenteFrequenceHarmonique

        app = Ursina()
        EditorCamera()
        precedenteFrequenceFondamentale, precedenteFrequenceHarmonique = 0, 0

        def update():
            if self.q.qsize() > 0:
                frequence_fondamentale, frequence_harmonique = self.q.get()[0][0], self.q.get()[0][0]

                print(f"taille de la queue : {self.q.qsize()}")
                print("update")
                global precedenteFrequenceHarmonique, precedenteFrequenceFondamentale, pos_precedante
                if not precedenteFrequenceFondamentale:
                    precedenteFrequenceFondamentale, precedenteFrequenceHarmonique, pos_precedante = 0, 0, (0, 0, 0)
                position_x, position_y, position_z = calcul_position(frequence_fondamentale,
                                                                                    frequence_harmonique,
                                                                                    pos_precedante,
                                                                                    (precedenteFrequenceFondamentale,
                                                                                     precedenteFrequenceHarmonique))
                precedenteFrequenceFondamentale = frequence_fondamentale
                precedenteFrequenceHarmonique = frequence_harmonique

                cube = spatial.Cube((position_x, position_y, position_z), (self.r, self.g, self.b, 0.5))
                print("J'ai posé un cube :)")
                pos_precedante = (position_x, position_y, position_z)

        cubePremier = spatial.Cube((0, 0, 0), color.black)

        def update_task(task):
            update()
            return task.cont  # Continue d'exécuter cette tâche à chaque frame

        app.taskMgr.add(update_task)
        app.run()
