from django.db import models


class CadastroModel(models.Model):
    name = models.CharField(max_length=80)
    telephone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
