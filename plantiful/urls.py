"""
URL configuration for plantiful project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "plantiful"
urlpatterns = [
    path("", views.index, name="index"),
    path("containers", views.all_containers, name="all_containers"),
    path("container/new", views.new_container, name="new_container"),
    path("container/<int:container_id>", views.container, name="container"),
    path(
        "container/<int:container_id>/relocation",
        views.container_relocation,
        name="container_relocation",
    ),
    path(
        "container/<int:container_id>/relocation/new",
        views.new_relocation,
        name="new_relocation",
    ),
    path(
        "container/<int:container_id>/resoil",
        views.container_resoil,
        name="container_resoil",
    ),
    path("container/<int:container_id>/resoil/new", views.new_resoil, name="new_resoil"),
    path(
        "container/<int:container_id>/transplant",
        views.container_transplant,
        name="container_transplant",
    ),
    path("relocation/<int:relocation_id>", views.relocation, name="relocation"),
    path("resoil/<int:resoil_id>", views.resoil, name="resoil"),
    path("species", views.all_species, name="all_species"),
    path("species/new", views.new_species, name="new_species"),
    path("species/<int:species_id>", views.species, name="species"),
    path("plants", views.all_plants, name="all_plants"),
    path("plant/new", views.new_plant, name="new_plant"),
    path("plant/<int:plant_id>", views.plant, name="plant"),
    path("plant/<int:plant_id>/harvest", views.plant_harvest, name="plant_harvest"),
    path("plant/<int:plant_id>/harvest/new", views.new_harvest, name="new_harvest"),
    path("plant/<int:plant_id>/fertilize", views.plant_fertilize, name="plant_fertilize"),
    path("plant/<int:plant_id>/fertilize/new", views.new_fertilize, name="new_fertilize"),
    path("plant/<int:plant_id>/mulch", views.plant_mulch, name="plant_mulch"),
    path("plant/<int:plant_id>/mulch/", views.new_mulch, name="new_mulch"),
    path(
        "plant/<int:plant_id>/observation",
        views.plant_observation,
        name="plant_observation",
    ),
    path(
        "plant/<int:plant_id>/observation/new",
        views.new_observation,
        name="new_observation",
    ),
    path("plant/<int:plant_id>/prune", views.plant_prune, name="plant_prune"),
    path("plant/<int:plant_id>/prune/new", views.new_prune, name="new_prune"),
    path(
        "plant/<int:plant_id>/relocation",
        views.plant_relocation,
        name="plant_relocation",
    ),
    path("plant/<int:plant_id>/resoil", views.plant_resoil, name="plant_resoil"),
    path(
        "plant/<int:plant_id>/transplant",
        views.plant_transplant,
        name="plant_transplant",
    ),
    path(
        "plant/<int:plant_id>/transplant/new",
        views.new_transplant,
        name="new_transplant",
    ),
    path("plant/<int:plant_id>/water", views.plant_water, name="plant_water"),
    path("plant/<int:plant_id>/water/new", views.new_water, name="new_water"),
    path("produce", views.all_produce, name="all_produce"),
    path("produce/new", views.new_produce, name="new_produce"),
    path("produce/<int:produce_id>", views.produce, name="produce"),
    path("harvest/<int:harvest_id>", views.harvest, name="harvest"),
    path("observation/<int:observation_id>", views.observation, name="observation"),
    path("water/<int:water_id>", views.water, name="water"),
    path("prune/<int:prune_id>", views.prune, name="prune"),
    path("fertilize/<int:fertilize_id>", views.fertilize, name="fertilize"),
    path("mulch/<int:mulch_id>", views.mulch, name="mulch"),
    path("transplant/<int:transplant_id>", views.transplant, name="transplant"),
    path("admin/", admin.site.urls),
]
