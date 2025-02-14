# Importer les modules
from scipy.io import wavfile

def renvoyer_SignalAudio(fichier) :
    """Renvoie un tableau contenant toutes les amplitude de l'audio"""
    file_path = fichier
    sampling_rate, audio_signal = wavfile.read(file_path) 
    nombres_echantillons = len(audio_signal)
    durée = nombres_echantillons / sampling_rate  
    print(durée)

    return(audio_signal,nombres_echantillons,durée)
