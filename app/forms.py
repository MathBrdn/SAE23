from django import forms
from .models import Aeroport, Piste, Compagnie, TypeAvion, Avion, Vol


class AeroportForm(forms.ModelForm):
    class Meta:
        model = Aeroport
        fields = ['nom', 'pays']
        labels = {
            'nom': 'Nom',
            'pays': 'Pays',
        }


class PisteForm(forms.ModelForm):
    class Meta:
        model = Piste
        fields = ['numero', 'aeroports', 'longueur']
        labels = {
            'numero': 'Numéro',
            'aeroports': 'Aéroport',
            'longueur': 'Longueur (m)',
        }


class CompagnieForm(forms.ModelForm):
    class Meta:
        model = Compagnie
        fields = ['nom', 'description', 'pays_attache']
        labels = {
            'nom': 'Nom',
            'description': 'Description',
            'pays_attache': 'Pays de rattachement',
        }
class TypeAvionForm(forms.ModelForm):
    class Meta:
        model = TypeAvion
        fields = ['marque', 'modele', 'description', 'image', 'longueur_piste_necessaire']
        labels = {
            'marque': 'Marque',
            'modele': 'Modèle',
            'description': 'Description',
            'image': 'Image',
            'longueur_piste_necessaire': 'Longueur de pistes nécessaire (m)',
        }


class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['nom', 'compagnies', 'modele']
        labels = {
            'nom': 'Nom',
            'compagnies': 'Compagnie',
            'modele': 'Modèle',
        }


class VolForm(forms.ModelForm):
    class Meta:
        model = Vol
        fields = 'all'
        widgets = {
            'date_heure_depart': forms.DateTimeInput(attrs={'type_avions': 'datetime-local'}),
            'date_heure_arrivee': forms.DateTimeInput(attrs={'type_avions': 'datetime-local'}),
        }
        labels = {
            'avions': 'Avion',
            'pilote': 'Pilote',
            'aeroport_depart': 'Aéroport de Départ',
            'date_heure_depart': 'Date et Heure de Départ',
            'aeroport_arrivee': "Aéroport d'Arrivée",
            'date_heure_arrivee': "Date et Heure d'Arrivée",
        }


class VolUploadForm(forms.Form):
    fichier = forms.FileField(label='Sélectionnez un fichier CSV')