from django.shortcuts import render

#Temporary Database - REMOVE AFTER ADDING CAT MODEL
finches = [
    {'name': 'Sweetie',
     'sex': 'male',
     'species': 'pine grosbeak',
     'color': 'red',
     'description' : 'Absurdly tame, allowing very close approach.'},
    {'name': 'Honey',
     'sex': 'female',
     'species': 'American goldfinch',
     'color': 'yellow',
     'description': 'Flocks of goldfinches congregate in weedy fields, making musical and plaintive calls.'},
    {'name': 'Kuku',
     'sex': 'male',
     'species': 'purple finch',
     'color': 'brown',
     'description': 'They feed up in trees and on the ground in open woods.'}
]

def home(request):
    return render(request, 'home.html')