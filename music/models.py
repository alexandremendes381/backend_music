from django.db import models

# Create your models here.


class ArquivosModel(models.Model):
    imagem_play = models.ImageField(upload_to='imagens/')
    music_play = models.FileField(upload_to='musicas/')
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)

    def __str__(self):
        return f"Imagem: {self.imagem_play.name}, Música: {self.music_play.name}"
