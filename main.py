from modules import interface,enregistrement_audio,analyse_audio,generer_video,fondQuiChangeDeCouleur,calculRGB
import time
"""Interface1 = interface.Interface("OeuvreVisuelVocal","400x150")
Interface1.ajout_label("Bienvenue sur OeuvreVisuelVocal",0,0,(0,0),(30,0))
Interface1.ajout_button("Enregistrer l'audio",1,0,(0,0),(0,0),enregistrement_audio.Audio().enregistrer_audio)
Interface1.lancer_interface()

signal_audio_amplitude, nombre_echantillons, durée = analyse_audio.renvoyer_SignalAudio("tests/audios/20250131112752672100.wav")
audioToVideo = generer_video.AudioToVideo(signal_audio_amplitude,nombre_echantillons,durée)

start1 = time.time()
audioToVideo.generer_images_amplitude_ronds()
audioToVideo.creer_video()
end1 = time.time()
print("Temps d'execution : " + str(end1-start1))
start2 = time.time()
audioToVideo = generer_video.AudioToVideo(signal_audio_amplitude,nombre_echantillons,durée)
audioToVideo.generer_images_amplitude_carre()
audioToVideo.creer_video()
end2 = time.time()
print("Temps d'execution : " + str(end2-start2))"""

signal_audio_amplitude, nombre_echantillons, durée = analyse_audio.renvoyer_SignalAudio("tests/audios/20250131112752672100.wav")
max = max(signal_audio_amplitude)
screen = fondQuiChangeDeCouleur.ecran(0,0,0,signal_audio_amplitude)
screen.lancer()
<<<<<<< Updated upstream

=======
end1 = time.time()
print("Temps d'execution : " + str(end1-start1))

Interface1.supprimer_fichier()
>>>>>>> Stashed changes
