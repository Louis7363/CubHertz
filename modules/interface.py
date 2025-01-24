import customtkinter as ctk

"""app = ctk.CTk()
app.title('OeuvreVisuelVocal')
app.geometry("400x150")

labelBienvenue = ctk.CTkLabel(app, text="Bienvenue sur OeuvreVisuelVocal")
labelBienvenue.grid(row = 0, column = 0, padx=(10,0) ,pady=(30,10))

buttonEnregistrer = ctk.CTkButton(app, text="Enregistrer l'audio",command=enregistrement_audio.Audio().enregistrer_audio)
buttonEnregistrer.grid(row = 1, column = 0, padx = (10,0) ,pady = (10,0))

app.grid_columnconfigure(0,weight=1) #permet de configurer la column pour qu'elle prenne toute la largeur (permet de centrer les composants)
app.mainloop()
"""

class Interface :
    def __init__(self,title,geometry):
        self.app = ctk.CTk()
        self.title = title
        self.geometry = geometry

    def ajout_label(self,texte,row,column,padx,pady) :
        label = ctk.CTkLabel(self.app, text=texte)
        label.grid(row = row,column = column, padx=padx,pady=pady)

    def ajout_button(self,texte,row,column,padx,pady,fonction) :
        button = ctk.CTkButton(self.app,text=texte,command=fonction)
        button.grid(row=row,column=column,padx=padx,pady=pady)
    
    def lancer_interface(self) :
        self.app.grid_columnconfigure(0,weight=1)
        self.app.title(self.title)
        self.app.geometry(self.geometry)
        self.app.mainloop()