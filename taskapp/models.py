from django.db import models

# Create your models here.
class Widget(models.Model):
    name = models.CharField(max_length=140)

    # def __init__(self, name):
    #     self.name = name
