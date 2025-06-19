from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from .models import Avion

class AeroportForm(ModelForm):
    class Meta :
        model = models.Aeroport
        fields = ('nom', 'pays')
        labels = {
            'nom' : _('Nom'),
            'pays' : _('Pays'),
        }

class PisteForm(ModelForm):
    class Meta :
        model = models.Piste
        fields = ('aeroport', 'longueur')
        labels = {
            'aeroport' : _('Aéroport'),
            'longueur' : _('Longueur'),
        }


class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['nom', 'compagnie', 'modele']


class CompagnieForm(ModelForm):
    class Meta :
        model = models.Compagnie
        fields = ('nom', 'pays_attache','description')
        labels = {
            'nom' : _('Nom'),
            'pays_attache' : _("Pays de rattachement"),
            'description' : _('Déscription'),
        }

class TypeAvionForm(ModelForm):
    class Meta:
        model = models.TypeAvion
        fields = ('marque', 'modele', 'description', 'longueur_piste_necessaire', 'image')
        labels = {
            'marque': _('Nom'),
            'modele': _('Modèle'),
            'description': _('Description'),
            'longueur_piste_necessaire': _('Longueur de piste nécessaire'),
            'image': _('Image'),
        }


class VolForm(ModelForm):
    class Meta :
        model = models.Vol
        fields =('avion', 'pilote', 'aeroport_depart', 'date_heure_depart', 'aeroport_arrivee', 'date_heure_arrivee')
        labels = {
            'avion' : _('Avion'),
            'pilote' : _('Pilote'),
            'aeroport_depart' : _('Aeroport de départ'),
            "date_heure_depart" : _("Date et heure de départ"),
            'aeroport_arrivee' : _("Aeroport d'arrivee"),
            'date_heure_arrivee' : _("Date et heure d'arrivee"),
        }