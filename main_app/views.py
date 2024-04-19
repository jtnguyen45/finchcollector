from django.shortcuts import render

#Temporary Database - REMOVE AFTER ADDING CAT MODEL


def home(request):
    return render(request, 'home.html')