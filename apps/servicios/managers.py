from django.db import models

class ServicioManager(models.Manager):
    def lista_servicios(self):
        service=self.all()
        return service