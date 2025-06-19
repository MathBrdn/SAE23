from django.db import models
import bleach

class Aeroport(models.Model):
    nom = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)

    def __str__(self):
        return f"Aeroport {self.nom} - ({self.pays})"
    
class Piste(models.Model):
    numero = models.IntegerField(blank = False, null = False)
    aeroport = models.ForeignKey("aeroport", on_delete=models.CASCADE)
    longueur = models.IntegerField()

    def str(self):
        return f"Piste {self.aeroport} - {self.longueur}"

class Compagnie(models.Model):
    id_compagnie = models.IntegerField(blank = False, null = False)
    nom = models.CharField(max_length=50)
    description = models.TextField()
    pays_attache = models.CharField(max_length=50)
    
    def str(self):
        return f"Compagnie {self.nom} - {self.pays_attache} - {self.description}"

class TypeAvion(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=100)
    description = models.TextField()
    longueur_piste_necessaire = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.marque} - {self.modele}"

    def str(self):
        return f"Type d'avion {self.marque} - {self.modele} - {self.image} - {self.longueur_piste_necessaire} - {self.description}"

class Avion(models.Model):
    nom = models.CharField(max_length=50)
    compagnie = models.ForeignKey("Compagnie", on_delete=models.CASCADE)
    modele = models.ForeignKey("TypeAvion", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} ({self.modele})"



class Vol(models.Model):
    id_vol = models.IntegerField(blank = False, null = False)
    avion = models.ForeignKey("avion", on_delete=models.CASCADE)
    pilote = models.CharField(max_length=50)
    aeroport_depart = models.ForeignKey("aeroport", related_name='depart_vols', on_delete=models.CASCADE)
    date_heure_depart = models.DateField()
    aeroport_arrivee = models.ForeignKey("aeroport", related_name='arrivee_vols', on_delete=models.CASCADE)
    date_heure_arrivee = models.DateField()

    def str(self):
        return f"Vol {self.avion.nom} - {self.aeroport_depart.nom} - {self.date_heure_depart} - {self.aeroport_arrivee.nom} - {self.date_heure_arrivee}"
