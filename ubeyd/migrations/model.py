__author__ = 'ubeydullahyuruk'

from django.db import models
class Publisher(models.Model):
    name = models.CharField(max_length=30)
