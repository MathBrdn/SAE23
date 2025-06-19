from django.shortcuts import render, redirect, get_object_or_404
from .forms import AeroportForm
from .models import Aeroport

def home(request):
    return render(request, "app/home.html")

def index(request):
    liste = Aeroport.objects.all()
    return render(request, "app/aeroport/index.html", {"liste": liste})

def create(request):
    if request.method == "POST":
        form = AeroportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aeroport_list') 
    else:
        form = AeroportForm()
    return render(request, "app/aeroport/form.html", {"form": form})

def affiche(request, id):
    aeroport = get_object_or_404(Aeroport, pk=id)
    return render(request, "app/aeroport/detail.html", {"aeroport": aeroport})

def update(request, id):
    aeroport = get_object_or_404(Aeroport, pk=id)
    if request.method == "POST":
        form = AeroportForm(request.POST, instance=aeroport)
        if form.is_valid():
            form.save()
            return redirect('aeroport_list')
    else:
        form = AeroportForm(instance=aeroport)
    return render(request, "app/aeroport/form.html", {"form": form})

def delete(request, id):
    aeroport = get_object_or_404(Aeroport, pk=id)
    aeroport.delete()
    return redirect('aeroport_list')
