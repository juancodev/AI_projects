from django.db import models

"""
  En models, creamos la clase que vamos a utilizar para los modelos de datos que se van a migrar a nuestra db

  # 1.- Cuando hagamos textos cortos, utilizamos CharField pero cuando sean textos más largos como artículos o blogs, utilizamos TextField.

  # 2.- Cuando hagamos relaciones entre tablas, necesitamos utilizar de models, el método ForeignKey y dentro de los paréntesis debe ir la tabla.
"""


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    # 1
    title = models.CharField(max_length=200)
    description = models.TextField()
    # 2
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
