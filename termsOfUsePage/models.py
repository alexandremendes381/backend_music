from django.db import models


class termsModel(models.Model):
    termosText = models.TextField()

    def __str__(self):
        return self.termosText
