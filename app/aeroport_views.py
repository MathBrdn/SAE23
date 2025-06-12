from django.shortcuts import render, HttpResponseRedirect
from .forms import AeroportForm
from . import models

def create(request):
    if request.method == "POST":
        form = AeroportForm(request)
        return render(request, "app/aeroport/create.html",{"form" : form})
    else:
        form = AeroportForm()
        return render(request, "app/aeroport/create.html",{"form" : form})

def traitement(request):
    lform = AeroportForm(request.POST)
    if lform.is_valid():
        aeroport = lform.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/aeroport/create.html",{"form" : lform})

def index(request):
    liste = list(models.Aeroport.objects.all())
    return render(request, "app/aeroport/index.html",{"liste" : liste})

def affiche(request, id):
    aeroport = models.Aeroport.objects.get(pk = id)
    return render(request, "app/aeroport/traitement.html", {"aeroport" : aeroport})

def update(request, id):
    aeroport = models.Aeroport.objects.get(pk=id)
    form = AeroportForm(aeroport.dico())
    return render(request, "app/aeroport/update.html",{"form": form, "id" : id})

def updatetraitement(request, id):
    lform = AeroportForm(request.POST)
    if lform.is_valid():
        aeroport = lform.save(commit = False)
        aeroport.id = id
        aeroport.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/aeroport/update.html",{"form" : lform, "id" : id})

def delete(request, id):
    aeroport =models.Aeroport.objects.get(pk = id)
    aeroport.delete()
    return HttpResponseRedirect("/app/index")


def home(request):
    return render(request, "app/aeroport/home.html")

    

