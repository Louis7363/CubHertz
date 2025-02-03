from PIL import Image, ImageDraw
def rond(amplitude,max) :
    rayon = abs((amplitude/max)*300)
    #print(amplitude,max,rayon)
    im = Image.new('RGB', (500, 300), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    return rayon,im,draw
def carre(amplitude,max) :
    cote = abs((amplitude/max)*300)
    im = Image.new('RGB', (500, 300), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    return cote,im,draw
