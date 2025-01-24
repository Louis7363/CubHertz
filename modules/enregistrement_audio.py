import pyaudio
import wave

class Audio :
    """Class Audio ayant comme méthode : enregistrement_audio qui permet d'enregister un audio"""
    def __init__(self,name):
        self.format = pyaudio.paInt16 #format sur 16 bits
        self.channels = 2 #nombres de cannaux d'entrées
        self.rate = 44100 # Spécifie le taux souhaité en Hz
        self.chunk = 1024 #nombre d'échantillons collectés par seconde
        self.record_seconds = 5 #nombres de secondes d'écoute
        self.filename = name #nom donné au fichier
    def enregistrement_audio(self) :
        audio = pyaudio.PyAudio()
        # Debut enregistrement
        stream = audio.open(format=self.format, channels=self.channels,
                        rate=self.rate, input=True,
                        frames_per_buffer=self.chunk)
        print("Enregistrement en cours...")
        
        frames = []
        
        for i in range(0, int(self.rate / self.chunk * self.record_seconds)):
            data = stream.read(self.chunk)
            frames.append(data)
            
        print("Fin d'enregistrement")
        # Fin enregistrement
        stream.stop_stream()
        stream.close()
        audio.terminate()
        self.enregistrement_fichier(audio,frames)
    def enregistrement_fichier(self,audio,frames) :
        waveFile = wave.open(self.filename, 'wb')
        waveFile.setnchannels(self.channels) #défini le nombre de canaux
        waveFile.setsampwidth(audio.get_sample_size(self.format)) #définit la largeur de de l'échantillon sur 16 bits(format défini dans l'initialisation de la classe)
        waveFile.setframerate(self.rate)  #règle la fréquence d'image sur 44100 Hz (defini dans l'initialisation de la classe)
        waveFile.writeframes(b''.join(frames)) #écrit les frames de l'audio
        waveFile.close()

audio1 = Audio("test.wav")
audio1.enregistrement_audio()
