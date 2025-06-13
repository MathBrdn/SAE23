from django.shortcuts import render, HttpResponseRedirect
from .forms import PisteForm
from . import models

def create2(request):
    if request.method == "POST":
        form = PisteForm(request)
        return render(request, "app/piste/create.html",{"form" : form})
    else:
        form = PisteForm()
        return render(request, "app/piste/create.html",{"form" : form})

def traitement2(request):
    lform = PisteForm(request.POST)
    if lform.is_valid():
        piste = lform.save()
        return HttpResponseRedirect("/app/")
    else:
        return render(request, "app/piste/create.html",{"form" : lform})

def index2(request):
    liste = list(models.Piste.objects.all())
    return render(request, "app/piste/index.html",{"liste" : liste})

def affiche2(request, id):
    piste = models.Piste.objects.get(pk = id)
    return render(request, "app/piste/traitement.html", {"piste" : piste})

def update2(request, id):
    piste = models.Piste.objects.get(pk=id)
    form = PisteForm(piste.dico())
    return render(request, "app/piste/update.html",{"form": form, "id" : id})

def updatetraitement2(request, id):
    lform = PisteForm(request.POST)
    if lform.is_valid():
        piste = lform.save(commit = False)
        piste.id = id
        piste.save()
        return HttpResponseRedirect("/app/")
    else:
        return render(request, "app/piste/update.html",{"form" : lform, "id" : id})

def delete2(request, id):
    piste =models.Piste.objects.get(pk = id)
    piste.delete()
    return HttpResponseRedirect("/app/")