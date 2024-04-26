from django.contrib import admin
from .models import Finch, Feeding, Sighting, Diet

# Register your models here.
admin.site.register([Finch, Feeding, Sighting, Diet])