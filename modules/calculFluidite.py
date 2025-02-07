def calculFluidite(r1,g1,b1,r10,g10,b10):
    rapportR = r1-r10
    rapportG = g1-g10
    rapportB = b1-b10
    return rapportR/100,rapportG/100,rapportB/100