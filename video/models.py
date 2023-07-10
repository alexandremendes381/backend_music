from django.db import models


class Video(models.Model):
    imagem_play = models.ImageField(upload_to='videos/imagem')
    video_file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
