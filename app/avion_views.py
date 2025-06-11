from django.shortcuts import render, HttpResponseRedirect
from .forms import AvionForm
from . import models

def create3(request):
    if request.method == "POST":
        form = AvionForm(request)
        return render(request, "app/avion/create.html",{"form" : form})
    else:
        form = AvionForm()
        return render(request, "app/avion/create.html",{"form" : form})

def traitement3(request):
    lform = AvionForm(request.POST)
    if lform.is_valid():
        avion = lform.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/avion/create.html",{"form" : lform})

def index3(request):
    liste = list(models.Avion.objects.all())
    return render(request, "app/avion/index.html",{"liste" : liste})

def affiche3(request, id):
    avion = models.Avion.objects.get(pk = id)
    return render(request, "app/avion/traitement.html", {"avion" : avion})

def update3(request, id):
    avion = models.Avion.objects.get(pk=id)
    form = AvionForm(avion.dico())
    return render(request, "app/avion/update.html",{"form": form, "id" : id})

def updatetraitement3(request, id):
    lform = AvionForm(request.POST)
    if lform.is_valid():
        avion = lform.save(commit = False)
        avion.id = id
        avion.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/avion/update.html",{"form" : lform, "id" : id})

def delete3(request, id):
    avion =models.Avion.objects.get(pk = id)
    avion.delete()
    return HttpResponseRedirect("/app/index")