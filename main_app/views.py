from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {
        'finch' : finch
    })

# Class-based Views
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'sex', 'species', 'color', 'description']
    success_url = '/finches/{id}'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'color', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'