from django.db import models

# Create your models here.
#fanaovana creation table.
class Maison (models.Model):
    type=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    