def RapportCouleur(r1,g1,b1,r100,g100,b100):
    rapportR = r100-r1
    rapportG = g100-g1
    rapportB = b100-b1
    return rapportR/500,rapportG/500,rapportB/500#

def RapportPosition(pos1,posFin) :
    rapport = posFin - pos1
    return rapport/500