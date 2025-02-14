from modules import enregistrement_audio
import time
import customtkinter as ctk
import os

class Interface :
    def __init__(self, title, geometry):
        self.app = ctk.CTk()
        self.title = title

        self.geometry = geometry

        label = ctk.CTkLabel(self.app, text= "Bienvenue sur OeuvreVisuelVocal")
        label.grid(row = 0, column = 0, padx=(0,0), pady=(30,0))

        self.button = ctk.CTkButton(self.app, text="commencer l'enregistrement", command=self.commencer_enregistrement_interface)
        self.button.grid(row=1, column=0, padx=(0,0), pady=(20,0))

        self.audio = enregistrement_audio.Audio()

    def renvoyer_nom_audio(self):
        return self.audio.filename
    
    def commencer_enregistrement_interface(self) :
        self.audio.commencer_enregistrement()
        self.button.configure(text="Arrêter l'enregistrement", command=self.arreter_enregistrement_interface)

    def arreter_enregistrement_interface(self):
        self.audio.arreter_enregistrement()
        time.sleep(1)
        self.app.destroy()

    def lancer_interface(self) :
        self.app.grid_columnconfigure(0,weight=1)
        self.app.title(self.title)
        self.app.geometry(self.geometry)
        self.app.mainloop()

    def supprimer_fichier(self) :
        filename = self.audio.filename
        print()
        try :
            os.remove(filename)
            print(f"le fichier '{filename}' a bien été supprimé")
        
        except FileNotFoundError:
            print(f"le fichier '{filename}' n a pas été trouvé")

