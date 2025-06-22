# Projet : CubHertz
# Auteurs : Louis Colbert, Luc Vallet

import numpy as np
from numpy.fft import fft, fftfreq
def fourrier(tab) :
    tab_freq_fondamentale = []
    tab_freq_harmonique = []
    for i in range(0,len(tab),1000) :
        tabTempo = tab[i:i+1000]
        Te = 0.0001
        N = len(tabTempo)
        # Calcul FFT
        X = fft(tabTempo)  # Transformée de fourier
        freq = fftfreq(tabTempo.size, d=Te)  # Fréquences de la transformée de Fourier

        # On prend la valeur absolue de l'amplitude uniquement pour les fréquences positives
        X_abs = np.abs(X[:N//2])
        # Normalisation de l'amplitude
        X_norm = X_abs*2.0/N
        # On garde uniquement les fréquences positives
        freq_pos = freq[:N//2]
        AmpliFondamentale = np.argmax(X_norm)
        frequFondamentale = freq_pos[AmpliFondamentale]

        start_index = max(0, AmpliFondamentale - 100)
        end_index = min(len(X_norm), AmpliFondamentale + 100)

        X_normF = X_norm[:start_index]
        X_normL = X_norm[end_index:]

        X_norm = np.concatenate((X_normF, X_normL))
        freq_posF = freq_pos[:start_index]
        freq_posL = freq_pos[end_index:]
        freq_pos = np.concatenate((freq_posF, freq_posL))
        AmpliHarmonique = np.argmax(X_norm)
        frequHarmonique = freq_pos[AmpliHarmonique]

        tab_freq_fondamentale.append(frequFondamentale)
        tab_freq_harmonique.append(frequHarmonique)

    print(tab_freq_fondamentale,tab_freq_harmonique)
    return tab_freq_fondamentale,tab_freq_harmonique