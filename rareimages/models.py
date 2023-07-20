from django.db import models

# Create your models here.


class ImagesModel(models.Model):
    images = models.FileField(upload_to='rareimages/')

    def __str__(self):
        return self.images
