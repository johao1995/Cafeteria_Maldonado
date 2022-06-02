from django.db import models

class VisitaManager(models.Manager):
    def lista_visitas(self):
        visita=self.all()
        return visita