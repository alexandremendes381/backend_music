from django.db import models


class CadastroModel(models.Model):
    selfie = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=80)
    birthdate = models.IntegerField()
    cep = models.CharField(max_length=10, default='')
    city = models.CharField(max_length=80, default='')
    uf = models.CharField(max_length=30, default='')
    bairro = models.CharField(max_length=80, default='')
    country = models.CharField(max_length=50, default='')
    telephone = models.CharField(max_length=20, null=True, unique=True)
    email = models.EmailField(null=True, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email
