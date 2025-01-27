import pyaudio
import wave
import datetime
class Audio :
    """Class Audio ayant comme méthode : enregistrement_audio qui permet d'enregister un audio"""
    def __init__(self):
        self.format = pyaudio.paInt16 #format sur 16 bits
        self.channels = 2 #nombres de cannaux d'entrées
        self.rate = 44100 # Spécifie le taux souhaité en Hz,  44 100 échantillons sont capturés chaque seconde
        self.chunk = 1024 #nombre d'échantillons correspondant à un bloc
        self.record_seconds = 5 #nombres de secondes d'écoute
        self.filename = self.creer_nom() #fonction pour créer un nom de fichier

    def creer_nom(self) :
        filename = 'tests/audios/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") +'.wav'
        return filename

    def enregistrer_audio(self) :
        audio = pyaudio.PyAudio()
        # Debut enregistrement
        stream = audio.open(format=self.format, channels=self.channels,
                        rate=self.rate, input=True,
                        frames_per_buffer=self.chunk)
        print("Enregistrement en cours...")
        
        frames = []
        #en divisant self.rate par self.chunk on obtient le nombre de frame nécessaire par secondes puis on multiplie par le nombre de secondes souhaités pour avoir le nombre de frame permettant de durer le temps souhaité
        for i in range(0, int(self.rate / self.chunk * self.record_seconds)):
            data = stream.read(self.chunk) #lis un bloc de l'audio de la taille de chunk soit 1024 par secondes
            frames.append(data)
            
        print("Fin d'enregistrement")
        # Fin enregistrement
        stream.stop_stream()
        stream.close()
        audio.terminate()
        self.enregistrer_fichier(audio,frames)

    def enregistrer_fichier(self,audio,frames) :
        waveFile = wave.open(self.filename, 'wb')
        waveFile.setnchannels(self.channels) #défini le nombre de canaux
        waveFile.setsampwidth(audio.get_sample_size(self.format)) #définit la largeur de de l'échantillon sur 16 bits(format défini dans l'initialisation de la classe)
        waveFile.setframerate(self.rate)  #règle la fréquence d'image sur 44100 Hz (defini dans l'initialisation de la classe)
        waveFile.writeframes(b''.join(frames)) #écrit les frames de l'audio
        waveFile.close()
