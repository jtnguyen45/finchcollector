from django.db import models
from django.urls import reverse

class Finch(models.Model):
    SEX_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS)
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )

    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default='B')
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
class Sighting(models.Model):
    ACTIONS = (
        ('F', 'Flying'),
        ('S', 'Sleeping'),
        ('D', 'Drinking water'),
        ('E', 'Eating'),
        ('M', 'Mating')
    )

    date = models.DateField('sighting date')
    where = models.CharField(max_length=100)
    action = models.CharField(max_length=1, choices=ACTIONS)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_action_display()} at {self.where} on {self.date}"
    
    class Meta:
        ordering = ['-date']