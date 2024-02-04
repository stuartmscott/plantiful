from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import (
    Container,
    Relocation,
    Resoil,
    Species,
    Plant,
    Transplant,
    Produce,
    Harvest,
    Observation,
    Water,
    Prune,
    Fertilize,
    Mulch,
    Death,
    Unit,
)


def index(request):
    context = {}
    return render(request, "plantiful/index.html", context)


def all_containers(request):
    container_list = Container.objects.all()
    context = {"container_list": container_list}
    return render(request, "plantiful/all_containers.html", context)


@login_required
def new_container(request):
    return HttpResponse("NOT YET IMPLEMENTED")


def container(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    return render(request, "plantiful/container.html", {"container": container})


def container_relocation(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    return render(request, "plantiful/container_relocation.html", {"container": container})


def container_resoil(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    return render(request, "plantiful/container_resoil.html", {"container": container})


def container_transplant(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    return render(request, "plantiful/container_transplant.html", {"container": container})


@login_required
def new_relocation(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    location = request.POST["location_name"]
    relocation = Relocation(datetime=timezone.now(), container=container, name=location)
    relocation.save()
    container.location = location
    container.save()
    return HttpResponseRedirect(reverse("container", args=(container_id,)))


def relocation(request, relocation_id):
    relocation = get_object_or_404(Relocation, pk=relocation_id)
    return render(request, "plantiful/relocation.html", {"relocation": relocation})


@login_required
def new_resoil(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    soil_type = request.POST["resoil_type"]
    resoil = Resoil(datetime=timezone.now(), container=container, type=soil_type)
    resoil.save()
    container.soil_type = soil_type
    container.save()
    return HttpResponseRedirect(reverse("container", args=(container_id,)))


def resoil(request, resoil_id):
    resoil = get_object_or_404(Resoil, pk=resoil_id)
    return render(request, "plantiful/resoil.html", {"resoil": resoil})


def all_species(request):
    species_list = Species.objects.all()
    context = {"species_list": species_list}
    return render(request, "plantiful/all_species.html", context)


@login_required
def new_species(request):
    return HttpResponse("NOT YET IMPLEMENTED")


def species(request, species_id):
    species = get_object_or_404(Species, pk=species_id)
    return render(request, "plantiful/species.html", {"species": species})


def all_plants(request):
    plant_list = Plant.objects.order_by("-datetime")
    context = {"plant_list": plant_list}
    return render(request, "plantiful/all_plants.html", context)


@login_required
def new_plant(request):
    return HttpResponse("NOT YET IMPLEMENTED")


def plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    latest_observation_list = plant.observation_set.order_by("-datetime")[:5]
    latest_water_list = plant.water_set.order_by("-datetime")[:5]
    latest_fertilize_list = plant.fertilize_set.order_by("-datetime")[:5]
    latest_mulch_list = plant.mulch_set.order_by("-datetime")[:5]
    latest_harvest_list = plant.harvest_set.order_by("-datetime")[:5]
    latest_prune_list = plant.prune_set.order_by("-datetime")[:5]
    return render(
        request,
        "plantiful/plant.html",
        {
            "plant": plant,
            "latest_observation_list": latest_observation_list,
            "latest_water_list": latest_water_list,
            "latest_fertilize_list": latest_fertilize_list,
            "latest_mulch_list": latest_mulch_list,
            "latest_harvest_list": latest_harvest_list,
            "latest_prune_list": latest_prune_list,
            "units": Unit.choices,
        },
    )


def plant_harvest(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    harvests = {}
    for produce in plant.species.produce_set.all():
        harvests[produce.name] = plant.harvest_set.filter(produce=produce.id)
    return render(
        request,
        "plantiful/plant_harvest.html",
        {"plant": plant, "plant_harvests": harvests, "units": Unit.choices},
    )


def plant_fertilize(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(
        request,
        "plantiful/plant_fertilize.html",
        {"plant": plant, "units": Unit.choices},
    )


def plant_mulch(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, "plantiful/plant_mulch.html", {"plant": plant, "units": Unit.choices})


def plant_observation(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(
        request,
        "plantiful/plant_observation.html",
        {"plant": plant, "units": Unit.choices},
    )


def plant_prune(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, "plantiful/plant_prune.html", {"plant": plant, "units": Unit.choices})


def plant_relocation(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    # TODO
    relocations = []
    return render(
        request,
        "plantiful/plant_relocation.html",
        {"plant": plant, "relocations": relocations, "units": Unit.choices},
    )


def plant_resoil(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    # TODO
    resoils = []
    return render(
        request,
        "plantiful/plant_resoil.html",
        {"plant": plant, "resoils": resoils, "units": Unit.choices},
    )


def plant_transplant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(
        request,
        "plantiful/plant_transplant.html",
        {"plant": plant, "units": Unit.choices},
    )


def plant_water(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, "plantiful/plant_water.html", {"plant": plant, "units": Unit.choices})


def transplant(request, transplant_id):
    transplant = get_object_or_404(Transplant, pk=transplant_id)
    return render(request, "plantiful/transplant.html", {"transplant": transplant})


def all_produce(request):
    produce_list = Produce.objects.all()
    context = {"produce_list": produce_list}
    return render(request, "plantiful/all_produce.html", context)


@login_required
def new_produce(request):
    return HttpResponse("NOT YET IMPLEMENTED")


def produce(request, produce_id):
    produce = get_object_or_404(Produce, pk=produce_id)
    return render(request, "plantiful/produce.html", {"produce": produce})


@login_required
def new_harvest(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    produce = get_object_or_404(Produce, pk=request.POST["produce_id"])
    harvest = Harvest(
        datetime=timezone.now(),
        plant=plant,
        produce=produce,
        weight=(
            request.POST["harvest_weight"] if "harvest_weight" in request.POST and request.POST["harvest_weight"] else 1
        ),
        unit=request.POST["harvest_unit"] if "harvest_unit" in request.POST else None,
    )
    harvest.save()
    return HttpResponseRedirect(reverse("plant", args=(plant_id,)))


def harvest(request, harvest_id):
    harvest = get_object_or_404(Harvest, pk=harvest_id)
    return render(request, "plantiful/harvest.html", {"harvest": harvest})


@login_required
def new_observation(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    observation = Observation(datetime=timezone.now(), plant=plant, text=request.POST["observation_text"])
    # image=request.POST["observation_image"])
    observation.save()
    return HttpResponseRedirect(reverse("plant", args=(plant_id,)))


def observation(request, observation_id):
    observation = get_object_or_404(Observation, pk=observation_id)
    return render(request, "plantiful/observation.html", {"observation": observation})


@login_required
def new_water(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    water = Water(
        datetime=timezone.now(),
        plant=plant,
        amount=(
            int(request.POST["water_amount"]) if "water_amount" and request.POST["water_amount"] in request.POST else 1
        ),
        unit=(request.POST["water_unit"] if "water_unit" in request.POST else Unit.LITRE[0]),
    )
    water.save()
    return HttpResponseRedirect(reverse("plant", args=(plant_id,)))


def water(request, water_id):
    water = get_object_or_404(Water, pk=water_id)
    return render(request, "plantiful/water.html", {"water": water})


@login_required
def new_prune(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    prune = Prune(
        datetime=timezone.now(),
        plant=plant,
        text=request.POST["prune_text"] if "prune_text" in request.POST else None,
    )
    prune.save()
    return HttpResponseRedirect(reverse("plant", args=(plant_id,)))


def prune(request, prune_id):
    prune = get_object_or_404(Prune, pk=prune_id)
    return render(request, "plantiful/prune.html", {"prune": prune})


@login_required
def new_fertilize(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    fertilize = Fertilize(
        datetime=timezone.now(),
        plant=plant,
        type=request.POST["fertilize_type"],
        amount=(
            int(request.POST["fertilize_amount"])
            if "fertilize_amount" and request.POST["fertilize_amount"] in request.POST
            else 1
        ),
        unit=(request.POST["fertilize_unit"] if "fertilize_unit" in request.POST else None),
    )
    fertilize.save()
    return HttpResponseRedirect(reverse("plant", args=(plant_id,)))


def fertilize(request, fertilize_id):
    fertilize = get_object_or_404(Fertilize, pk=fertilize_id)
    return render(request, "plantiful/fertilize.html", {"fertilize": fertilize})


@login_required
def new_mulch(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    mulch = Mulch(datetime=timezone.now(), plant=plant, type=request.POST["mulch_type"])
    mulch.save()
    return HttpResponseRedirect(reverse("plant", args=(plant_id,)))


def mulch(request, mulch_id):
    mulch = get_object_or_404(Mulch, pk=mulch_id)
    return render(request, "plantiful/mulch.html", {"mulch": mulch})


@login_required
def new_transplant(request, plant_id, container_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    container = get_object_or_404(Container, pk=container_id)
    transplant = Transplant(datetime=timezone.now(), plant=plant, container=container)
    transplant.save()
    plant.container = container_id
    plant.save()
    return HttpResponseRedirect(reverse("plant", args=(plant_id,)))


def transplant(request, transplant_id):
    transplant = get_object_or_404(Transplant, pk=transplant_id)
    return render(request, "plantiful/transplant.html", {"transplant": transplant})


@login_required
def new_death(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    death = Death(datetime=timezone.now(), plant=plant)
    death.save()
    return HttpResponseRedirect(reverse("plant", args=(plant_id,)))


def death(request, death_id):
    death = get_object_or_404(Death, pk=death_id)
    return render(request, "plantiful/death.html", {"death": death})
