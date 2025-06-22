#Projet : CubHertz
#Auteurs : Louis Colbert, Luc Vallet

import random

def calcul_position(frequence_fondamentale,frequence_harmonique,pos_precedente,freq_precedente):
    pos_precedente_x = pos_precedente[0]
    pos_precedente_y = pos_precedente[1]
    pos_precedente_z = pos_precedente[2]
    freq_precedente_fondamentale = freq_precedente[0]
    freq_precedente_harmonique = freq_precedente[1]
    pos_x,pos_y,pos_z = pos_precedente_x,pos_precedente_y,pos_precedente_z
    choix_x_or_y = random.randint(0,1)
    if frequence_fondamentale > freq_precedente_fondamentale:
        pos_z = pos_precedente_z + 1

    elif frequence_fondamentale < freq_precedente_fondamentale:
        pos_z = pos_precedente_z - 1

    if frequence_harmonique > freq_precedente_harmonique:
        if choix_x_or_y == 0:
            pos_x = pos_precedente_x + 0.5
        else:
            pos_y = pos_precedente_y + 0.5

    elif frequence_harmonique < freq_precedente_harmonique:
        if choix_x_or_y == 0:
            pos_x = pos_precedente_x - 0.5
        else:
            pos_y = pos_precedente_y - 0.5

    if pos_x == pos_precedente_x and pos_y == pos_precedente_y:
        pos_x += 1

    return pos_x,pos_y,pos_z
