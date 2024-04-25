from django.forms import ModelForm
from .models import Feeding, Sighting

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ('date', 'meal')

class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = ('date', 'where', 'action')