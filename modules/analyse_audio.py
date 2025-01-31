# Importer les modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
from pydub import AudioSegment

# Importer le fichier audio .wav
file_path = "tests/audios/20250131112752672100.wav"
sampling_rate, audio_signal = wavfile.read(file_path)
print(audio_signal)
print('Sampling Rate:', sampling_rate)
print('Audio Shape:', np.shape(audio_signal))

# Nombre d'échantillons
num_samples = audio_signal.shape[0]
print(num_samples)
# Durée de l'audio
audio_duration = num_samples / sampling_rate
print(audio_duration)

# Tracer le signal en fonction du temps
time_axis = np.linspace(0, audio_duration, num_samples) #tableau de valeur représentant le temps allant de 0 à la longueur total du temps de l'audio espacé avec num_samples
print(time_axis)


"""plt.subplot(2,1,1)
plt.plot(time_axis, audio_signal, 'b-') #audio signal correspond à l'amplitude du son dans le stéréo gauche et le stéréo droit"""


def renvoyer_SignalAudio(fichier) :
    """Renvoie un tableau contenant toutes les amplitude de l'audio"""
    file_path = fichier
    sampling_rate, audio_signal = wavfile.read(file_path)   
    return(audio_signal)



"""plt.ylabel('Gauche')
plt.xlabel('Temps (s)')
plt.show()"""
fr, tm, spgram = signal.spectrogram(audio_signal,sampling_rate)
lspg = np.log(spgram)
"""plt.pcolormesh(tm,fr,lspg,shading='auto')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (sec)')
plt.show()"""
