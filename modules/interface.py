import customtkinter as ctk
import enregistrement_audio

app = ctk.CTk()
app.title('OeuvreVisuelVocal')
app.geometry("400x150")

labelBienvenue = ctk.CTkLabel(app, text="Bienvenue sur OeuvreVisuelVocal")
labelBienvenue.grid(row = 0, column = 0, padx=(10,0) ,pady=(30,10))

buttonEnregistrer = ctk.CTkButton(app, text="Enregistrer l'audio",command=enregistrement_audio.Audio("TestInterface.wav").enregistrer_audio)
buttonEnregistrer.grid(row = 1, column = 0, padx = (10,0) ,pady = (10,0))

app.grid_columnconfigure(0,weight=1) #permet de configurer la column pour qu'elle prenne toute la largeur (permet de centrer les composants)
app.mainloop()

