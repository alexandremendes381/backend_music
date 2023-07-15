from django.db import models

# Create your models here.


class postsModel(models.Model):
    arquivo = models.FileField(upload_to='posts/')
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.imagem
