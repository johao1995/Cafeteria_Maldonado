from django.db import models

class BlogManager(models.Manager):
    def lista_blogs(self):
        blog=self.all()
        return blog