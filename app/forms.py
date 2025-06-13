from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

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

class AvionForm(ModelForm):
    class Meta :
        model = models.Avion
        fields = ('nom', 'compagnie', 'modele')
        labels = {
            'nom' : _('Nom'),
            'compagnie' : _('Compagnie'),
            'modele' : _('Modèle'),
        }

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
    class Meta :
        model = models.TypeAvion
        fields = ('marque', 'modele', 'image', 'longueur_piste_necessaire', 'description')
        labels = {
            'marque' : _('Nom'),
            'modele' : _('Modèle'),
            'image' : _('Image'),
            'longueur_piste_necessaire' : _('Longueur de piste nécessaire'),
            'description' : _('Déscription'),
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