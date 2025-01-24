from modules import interface,enregistrement_audio

Interface1 = interface.Interface("OeuvreVisuelVocal","400x150")
Interface1.ajout_label("Bienvenue sur OeuvreVisuelVocal",0,0,(10,0),(30,0))
Interface1.ajout_button("Enregistrer l'audio",1,0,(10,0),(10,0),enregistrement_audio.Audio().enregistrer_audio)
Interface1.lancer_interface()