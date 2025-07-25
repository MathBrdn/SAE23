from django.shortcuts import render, HttpResponseRedirect
from .forms import TypeAvionForm
from . import models

def create5(request):
    if request.method == "POST":
        form = TypeAvionForm(request)
        return render(request, "app/type/create.html",{"form" : form})
    else:
        form = TypeAvionForm()
        return render(request, "app/type/create.html",{"form" : form})

def traitement5(request):
    lform = TypeAvionForm(request.POST)
    if lform.is_valid():
        type = lform.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/type/create.html",{"form" : lform})

def index5(request):
    liste = list(models.TypeAvion.objects.all())
    return render(request, "app/type/index.html",{"liste" : liste})

def affiche5(request, id):
    type = models.TypeAvion.objects.get(pk = id)
    return render(request, "app/type/traitement.html", {"type" : type})

def update5(request, id):
    type = models.TypeAvion.objects.get(pk=id)
    form = TypeAvionForm(type.dico())
    return render(request, "app/type/update.html",{"form": form, "id" : id})

def updatetraitement5(request, id):
    lform = TypeAvionForm(request.POST)
    if lform.is_valid():
        type = lform.save(commit = False)
        type.id = id
        type.save()
        return HttpResponseRedirect("/app/index/")
    else:
        return render(request, "app/type/update.html",{"form" : lform, "id" : id})

def delete5(request, id):
    type =models.TypeAvion.objects.get(pk = id)
    type.delete()
    return HttpResponseRedirect("/app/index")
