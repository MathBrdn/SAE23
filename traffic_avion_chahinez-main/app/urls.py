from django.urls import path
from . import (
    home_views,
    aeroport_views,
    piste_views,
    avion_views,
    compagnie_views,
    type_views,
    vol_views
)


urlpatterns = [
    path('', aeroport_views.home, name='home'),

    # Aéroports
    path('aeroports/', aeroport_views.index, name='aeroport_list'),
    path('aeroports/create/', aeroport_views.create, name='aeroport_create'),
    path('aeroports/<int:id>/', aeroport_views.affiche, name='aeroport_detail'),
    path('aeroports/<int:id>/update/', aeroport_views.update, name='aeroport_update'),
    path('aeroports/<int:id>/delete/', aeroport_views.delete, name='aeroport_delete'),
    

    # Pistes
    path('pistes/', piste_views.index2, name='piste_list'),
    path('pistes/create/', piste_views.create2, name='piste_create'),
    path('pistes/<int:id>/', piste_views.affiche2, name='piste_detail'),
    path('pistes/<int:id>/update/', piste_views.update2, name='piste_update'),
    path('pistes/<int:id>/delete/', piste_views.delete2, name='piste_delete'),

    # Avions
    path('avions/', avion_views.index3, name='avion_list'),
    path('avions/create/', avion_views.create3, name='avion_create'),
    path('avions/<int:id>/', avion_views.affiche3, name='avion_detail'),
    path('avions/<int:id>/update/', avion_views.update3, name='avion_update'),
    path('avions/<int:id>/delete/', avion_views.delete3, name='avion_delete'),

    # Compagnies
    path('compagnies/', compagnie_views.index4, name='compagnie_list'),
    path('compagnies/create/', compagnie_views.create4, name='compagnie_create'),
    path('compagnies/<int:id>/update/', compagnie_views.update4, name='compagnie_update'),
    path('compagnies/<int:id>/delete/', compagnie_views.delete4, name='compagnie_delete'),

    # Types d'avions
    path('types-avions/', type_views.index5, name='typeavion_list'),
    path('types-avions/create/', type_views.create5, name='typeavion_create'),
    path('types-avions/<int:id>/update/', type_views.update5, name='typeavion_update'),
    path('types-avions/<int:id>/delete/', type_views.delete5, name='typeavion_delete'),

    # Vols
    path('vols/', vol_views.index6, name='vol_list'),
    path('vols/create/', vol_views.create6, name='vol_create'),
    path('vols/import/', vol_views.import_file, name='vol_import'),
    path('vols/recherche/', vol_views.search_flights, name='vol_recherche'),
]
