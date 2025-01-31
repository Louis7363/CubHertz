from modules import formes
import datetime
from moviepy import ImageSequenceClip
import os
class AudioToVideo() :
    def __init__(self,signal_audio_amplitude,nombre_echantillons,durée) :
        self.signal_audio_amplitude = signal_audio_amplitude
        self.nombre_echantillons = nombre_echantillons
        self.durée =  durée
        self.fps = 10000
        self.nombres_images_necessaire = durée * self.fps
        self.pas = int(self.nombre_echantillons/self.nombres_images_necessaire)
        self.max = max(signal_audio_amplitude)
        self.dossier = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

    def generer_images_amplitude_ronds(self) :
        for i in range (0,len(self.signal_audio_amplitude),self.pas ) :
            rayon,im,draw = formes.rond(self.signal_audio_amplitude[i],self.max)
            draw.circle(xy=(250,150) ,radius=rayon,fill=(255,0,0))
            if i == 0 :
                os.mkdir(path='tests/resultats/images/'+self.dossier)
            im.save(f'tests/resultats/images/{self.dossier}/image{int(i/self.pas)}.jpg', quality=95)

    def creer_video(self) :
        video = ImageSequenceClip('tests/resultats/images/'+self.dossier, fps=self.fps)
        print("Clip duration: {}".format(video.duration))
        print("Clip fps: {}".format(video.fps))
        video.write_videofile(f"tests/resultats/videos/{self.dossier}.mp4")
