from django.shortcuts import render, HttpResponseRedirect
from .forms import VolForm
from . import models

def create6(request):
    if request.method == "POST":
        form = VolForm(request)
        return render(request, "app/vol/create.html",{"form" : form})
    else:
        form = VolForm()
        return render(request, "app/vol/create.html",{"form" : form})

def traitement6(request):
    lform = VolForm(request.POST)
    if lform.is_valid():
        vol = lform.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/vol/create.html",{"form" : lform})

def index6(request):
    liste = list(models.Vol.objects.all())
    return render(request, "app/vol/index.html",{"liste" : liste})

def affiche6(request, id):
    vol = models.Vol.objects.get(pk = id)
    return render(request, "app/vol/traitement.html", {"vol" : vol})

def update6(request, id):
    vol = models.Vol.objects.get(pk=id)
    form = VolForm(vol.dico())
    return render(request, "app/vol/update.html",{"form": form, "id" : id})

def updatetraitement6(request, id):
    lform = VolForm(request.POST)
    if lform.is_valid():
        vol = lform.save(commit = False)
        vol.id = id
        vol.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/vol/update.html",{"form" : lform, "id" : id})

def delete6(request, id):
    vol =models.Vol.objects.get(pk = id)
    vol.delete()
    return HttpResponseRedirect("/app/index")

