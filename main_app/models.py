from django.db import models

class Finch(models.Model):
    SEX_OPTIONS = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    sex = models.CharField(choices=SEX_OPTIONS)
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.CharField(max_length=100)