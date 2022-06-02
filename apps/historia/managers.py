from django.db import models

class HistoryManager(models.Manager):
    def lista_historias(self):
        history=self.all()
        return history