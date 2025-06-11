from django.shortcuts import render, HttpResponseRedirect
from .forms import CompagnieForm
from . import models

def create4(request):
    if request.method == "POST":
        form = CompagnieForm(request)
        return render(request, "app/compagnie/create.html",{"form" : form})
    else:
        form = CompagnieForm()
        return render(request, "app/compagnie/create.html",{"form" : form})

def traitement4(request):
    lform = CompagnieForm(request.POST)
    if lform.is_valid():
        compagnie = lform.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/compagnie/create.html",{"form" : lform})

def index4(request):
    liste = list(models.Compagnie.objects.all())
    return render(request, "app/compagnie/index.html",{"liste" : liste})

def affiche4(request, id):
    compagnie = models.Compagnie.objects.get(pk = id)
    return render(request, "app/compagnie/traitement.html", {"compagnie" : compagnie})

def update4(request, id):
    compagnie = models.Compagnie.objects.get(pk=id)
    form = CompagnieForm(compagnie.dico())
    return render(request, "app/compagnie/update.html",{"form": form, "id" : id})

def updatetraitement4(request, id):
    lform = CompagnieForm(request.POST)
    if lform.is_valid():
        compagnie = lform.save(commit = False)
        compagnie.id = id
        compagnie.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/compagnie/update.html",{"form" : lform, "id" : id})

def delete4(request, id):
    compagnie =models.Compagnie.objects.get(pk = id)
    compagnie.delete()
    return HttpResponseRedirect("/app/index")