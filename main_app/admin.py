from django.contrib import admin
from .models import Finch, Feeding, Sighting

# Register your models here.
admin.site.register([Finch, Feeding, Sighting])