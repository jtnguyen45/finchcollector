from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Diet
from .forms import FeedingForm, SightingForm

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
    id_list = finch.diets.all().values_list('id')
    diets_finch_doesnt_have = Diet.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', {
        'finch' : finch,
        'feeding_form': feeding_form,
        'sighting_form': sighting_form,
        'diets': diets_finch_doesnt_have
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def add_sighting(request, finch_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_diet(request, finch_id, diet_id):
    Finch.objects.get(id=finch_id).diets.add(diet_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_diet(request, finch_id, diet_id):
    Finch.objects.get(id=finch_id).diets.remove(diet_id)
    return redirect('detail', finch_id=finch_id)

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

class DietList(ListView):
    model = Diet

class DietDetail(DetailView):
    model = Diet

class DietCreate(CreateView):
    model = Diet
    fields = '__all__'

class DietUpdate(UpdateView):
    model = Diet
    fields = ['name', 'amount']

class DietDelete(DeleteView):
    model = Diet
    success_url = '/diets'