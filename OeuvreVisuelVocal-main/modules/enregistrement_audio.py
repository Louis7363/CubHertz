import pyaudio
import wave
import datetime
import time
class Audio :
    """Class Audio ayant comme méthode : enregistrement_audio qui permet d'enregister un audio"""
    def __init__(self):
        self.format = pyaudio.paInt16 #format sur 16 bits
        self.channels = 1 #nombres de cannaux d'entrées
        self.rate = 5000 # Spécifie le taux souhaité en Hz,  44 100 échantillons sont capturés chaque seconde
        self.chunk = 10 #nombre d'échantillons correspondant à un bloc
        self.filename = self.creer_nom() #fonction pour créer un nom de fichier
        self.stream = None # attribut permettant de récuperer l'enregistrement brut
        self.audio = pyaudio.PyAudio() # carotte (un peu comme un micro)
        self.frames = [] # attribut contenant le fichier wav qui sera enregistré
        self.recording = False  # drapeau indiquant si l'enregistrement est en cours
        self.count = 0



    # fonction pour obtenir un nom de fichier selon la date
    def creer_nom(self) :
        filename = 'tests/audios/' + datetime.datetime.now().strftime("%m" + "_" + "%d" + "_" + "%H" + "_" + "%M" + "_" + "%S") + "__" + str(self.rate) +'.wav'
        return filename


    # fonction pour arreter l'enregistrement
    def commencer_enregistrement(self) :

        self.stream = self.audio.open(format=self.format, channels=self.channels,
                        rate=self.rate, input=True,
                        frames_per_buffer=self.chunk,
                        stream_callback=self.ecrire_arriere_plan)

        print("Enregistrement en cours...")

        self.stream.start_stream() # Debut enregistrement
        self.recording = True # on active le drapeau : "l'audio est en cours"
        
        
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
            self.enregistrer_fichier()

        print("Fin d'enregistrement")



    def enregistrer_fichier(self) :
        waveFile = wave.open(self.filename, 'wb')
        waveFile.setnchannels(self.channels) #défini le nombre de canaux
        waveFile.setsampwidth(self.audio.get_sample_size(self.format)) #définit la largeur de de l'échantillon sur 16 bits(format défini dans l'initialisation de la classe)
        waveFile.setframerate(self.rate)  #règle la fréquence d'image sur 44100 Hz (defini dans l'initialisation de la classe)
        waveFile.writeframes(b''.join(self.frames)) #écrit les frames de l'audio
        waveFile.close()

    def ecrire_arriere_plan(self, audio_entrant, nb_echantillons, time_info, status):
        self.frames.append(audio_entrant)
        print(self.chunk, len(audio_entrant), audio_entrant)
        print(nb_echantillons,time_info,status)
        if self.recording :
            flag = pyaudio.paContinue
        else :
            flag = pyaudio.paComplete
        return None, flag