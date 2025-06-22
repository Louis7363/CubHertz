# Rôles des différents fichiers
- Le fichier modules/calculPosition est chargé de calculer la position des cubes dans l'espace en fonction de la fréquence fondamentale,
de le fréquence harmonique, des fréquences qui ont placé le cube précédent. Cela renvoie les positions x,y et z du nouveau cube.
- Le fichier modules/calculRGB est chargé de calculer la couleur du cube en fonction de l'intensité du son. Cela renvoie les paramètres
de rouge de vert et de bleu.
- Le fichier modules/enregistrement_audio permet d'enregistrer le son et d'après envoyer le son avec une fonction callback pour faire les
calculs nécessaires pour la création du cube. 
- Le fichier modules/Fourrier permet en fonction d'un tableau d'intensité de calculer la fréquence fondamentale et la fréquence harmonique du passage audio
- le fichier modules/interface permet de créer l'interface qui enregistre possède le bouton pour lancer l'enregistrement
- le fichier modules/spatial contient la classe Cube qui ajoute un cube à l'interface.
- Le fichier main.py et le fichier principal que l'on doit executer et qui fait appel aux autres modules.

