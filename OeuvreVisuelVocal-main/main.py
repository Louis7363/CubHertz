import sys
from modules import interface,enregistrement_audio,analyse_audio,fondQuiChangeDeCouleur,calculRGB
import time

#from modules.ancienDossier import generer_video
Interface1 = interface.Interface("OeuvreVisuelVocal", "400x150")
nomAudio = Interface1.renvoyer_nom_audio()
Interface1.lancer_interface()

"""""
start1 = time.time()
sys.setrecursionlimit(10000)
signal_audio_amplitude, nombre_echantillons, durée = analyse_audio.renvoyer_SignalAudio(nomAudio)
max = max(signal_audio_amplitude)
screen = fondQuiChangeDeCouleur.ecran(0,0,0,signal_audio_amplitude)
screen.lancer()
end1 = time.time()
print("Temps d'execution : " + str(end1-start1))"""
Interface1.supprimer_fichier()