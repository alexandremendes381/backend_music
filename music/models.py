from django.db import models


def upload_music_to(instance, filename):
    artist_name = instance.artist.strip().lower()
    path = f"musicas/{artist_name}/{filename}"
    return path


def upload_image_to(instance, filename):
    artist_name = instance.artist.strip().lower()
    path = f"imagens/{artist_name}/{filename}"
    return path


class ArquivosModel(models.Model):
    imagem_play = models.ImageField(upload_to=upload_image_to)
    music_play = models.FileField(upload_to=upload_music_to)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)

    def __str__(self):
        return f"Imagem: {self.imagem_play.name}, Música: {self.music_play.name}"
