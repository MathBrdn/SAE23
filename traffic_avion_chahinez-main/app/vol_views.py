from django.shortcuts import render, HttpResponseRedirect
from .forms import VolForm
from . import models
from datetime import timedelta

def create6(request):
    if request.method == "POST":
        form = VolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vol_list')
    else:
        form = VolForm()
    return render(request, "app/vol/form.html", {"form": form})


def traitement6(request):
    lform = VolForm(request.POST)
    if lform.is_valid():
        vol = lform.save(commit=False)
        date_arrivee = vol.date_arrivee
        aeroport_arrivee = vol.aeroport_arrivee
        marge = timedelta(minutes=10)

        conflits = models.Vol.objects.filter(
            aeroport_arrivee=aeroport_arrivee,
            date_arrivee__range=(date_arrivee - marge, date_arrivee + marge)
        )

        if conflits.exists():
            nouvelle_arrivee = conflits.order_by('-date_arrivee').last().date_arrivee + marge
            vol.date_depart += (nouvelle_arrivee - date_arrivee)
            vol.date_arrivee = nouvelle_arrivee

        vol.save()
        return HttpResponseRedirect("/app/index6/")
    else:
        return render(request, "app/vol/create.html", {"form": lform})

def index6(request):
    liste = list(models.Vol.objects.all())
    return render(request, "app/vol/index.html", {"liste": liste})

def affiche6(request, id):
    vol = models.Vol.objects.get(pk=id)
    return render(request, "app/vol/traitement.html", {"vol": vol})

def update6(request, id):
    vol = models.Vol.objects.get(pk=id)
    form = VolForm(instance=vol)
    return render(request, "app/vol/update.html", {"form": form, "id": id})

def updatetraitement6(request, id):
    vol_existant = models.Vol.objects.get(pk=id)
    lform = VolForm(request.POST, instance=vol_existant)

    if lform.is_valid():
        vol = lform.save(commit=False)
        date_arrivee = vol.date_arrivee
        aeroport_arrivee = vol.aeroport_arrivee
        marge = timedelta(minutes=10)

        conflits = models.Vol.objects.filter(
            aeroport_arrivee=aeroport_arrivee,
            date_arrivee__range=(date_arrivee - marge, date_arrivee + marge)
        ).exclude(id=id)

        if conflits.exists():
            nouvelle_arrivee = conflits.order_by('-date_arrivee').last().date_arrivee + marge
            vol.date_depart += (nouvelle_arrivee - date_arrivee)
            vol.date_arrivee = nouvelle_arrivee

        vol.save()
        return HttpResponseRedirect("/app/index6/")
    else:
        return render(request, "app/vol/update.html", {"form": lform, "id": id})

def delete6(request, id):
    vol = models.Vol.objects.get(pk=id)
    vol.delete()
    return HttpResponseRedirect("/app/index6/")




import csv
from io import TextIOWrapper
from django.http import HttpResponse
from .models import Vol, Aeroport, Avion  # ajuste selon tes modèles

def import_file(request):
    if request.method == 'POST' and request.FILES.get('fichier'):
        fichier = request.FILES['fichier']
        data = TextIOWrapper(fichier.file, encoding='utf-8')
        reader = csv.DictReader(data, delimiter=',')

        for ligne in reader:
            try:
                Vol.objects.create(
                    numero=ligne['numero'],
                    date_depart=ligne['date_depart'],
                    date_arrivee=ligne['date_arrivee'],
                    aeroport_depart=Aeroport.objects.get(nom=ligne['aeroport_depart']),
                    aeroport_arrivee=Aeroport.objects.get(nom=ligne['aeroport_arrivee']),
                    avion=Avion.objects.get(id=ligne['avion_id'])
                )
            except Exception as e:
                return HttpResponse(f"Erreur dans le fichier : {e}")
        
        return HttpResponse("Importation terminée avec succès ✅")
    
    return render(request, 'app/import_vols.html')


from django.db.models import Q
from .models import Aeroport  # ajuste si besoin
from datetime import datetime

def search_flights(request):
    vols = []
    date = request.GET.get('date')
    aeroport_id = request.GET.get('aeroport')
    sens = request.GET.get('sens')

    if date and aeroport_id and sens:
        filtre = Q()
        if sens == 'depart':
            filtre &= Q(date_depart__date=date, aeroport_depart_id=aeroport_id)
        elif sens == 'arrivee':
            filtre &= Q(date_arrivee__date=date, aeroport_arrivee_id=aeroport_id)
        vols = models.Vol.objects.filter(filtre)

    aeroports = models.Aeroport.objects.all()
    return render(request, "app/vol/recherche.html", {
        'vols': vols,
        'aeroports': aeroports,
        'selected_date': date,
        'selected_aeroport': int(aeroport_id) if aeroport_id else None,
        'sens': sens
    })
