from django.urls import path
from . import aeroport_views, piste_views, avion_views, compagnie_views, type_views, vol_views

urlpatterns=[
    # page pour les aeroports
    path("create/", aeroport_views.create),
    path("traitement/", aeroport_views.traitement),
    path("index/", aeroport_views.index),
    path("affiche/<int:id>/", aeroport_views.affiche),
    path("update/<int:id>/", aeroport_views.update),
    path("updatetraitement/<int:id>/", aeroport_views.updatetraitement),
    path("delete/<int:id>/", aeroport_views.delete),
    # page pour les pistes
    path("create2/", piste_views.create2),
    path("traitement2/", piste_views.traitement2),
    path("", piste_views.index2),
    path("affiche2/<int:id>/", piste_views.affiche2),
    path("update2/<int:id>/", piste_views.update2),
    path("updatetraitement2/<int:id>/", piste_views.updatetraitement2),
    path("delete2/<int:id>/", piste_views.delete2),
    # page pour les avions
    path("create3/", avion_views.create3),
    path("traitement3/", avion_views.traitement3),
    path("index3/", avion_views.index3),
    path("affiche3/<int:id>/", avion_views.affiche3),
    path("update3/<int:id>/", avion_views.update3),
    path("updatetraitement3/<int:id>/", avion_views.updatetraitement3),
    path("delete3/<int:id>/", avion_views.delete3),
    # page pour les compagnies
    path("create4/", compagnie_views.create4),
    path("traitement4/", compagnie_views.traitement4),
    path("index4/", compagnie_views.index4),
    path("affiche4/<int:id>/", compagnie_views.affiche4),
    path("update4/<int:id>/", compagnie_views.update4),
    path("updatetraitement4/<int:id>/", compagnie_views.updatetraitement4),
    path("delete4/<int:id>/", compagnie_views.delete4),
    # page pour les types d'avion
    path("create5/", type_views.create5),
    path("traitement5/", type_views.traitement5),
    path("index5/", type_views.index5),
    path("affiche5/<int:id>/", type_views.affiche5),
    path("update5/<int:id>/", type_views.update5),
    path("updatetraitement5/<int:id>/", type_views.updatetraitement5),
    path("delete5/<int:id>/", type_views.delete5),
    # page pour les vols
    path("create6/", vol_views.create6),
    path("traitement6/", vol_views.traitement6),
    path("index6/", vol_views.index6),
    path("affiche6/<int:id>/", vol_views.affiche6),
    path("update6/<int:id>/", vol_views.update6),
    path("updatetraitement6/<int:id>/", vol_views.updatetraitement6),
    path("delete6/<int:id>/", vol_views.delete6),
]