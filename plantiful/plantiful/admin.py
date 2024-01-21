from django.contrib import admin

from .models import Container, Relocation, Resoil, Species, Plant, Transplant, Produce, Harvest, Observation, Water, Prune, Fertilize, Mulch, Death

class ContainerAdmin(admin.ModelAdmin):
    fields = ["name", "size", "location", "soil_type"]
    list_display = ["name", "location"]


admin.site.register(Container, ContainerAdmin)

class RelocationAdmin(admin.ModelAdmin):
    fields = ["datetime", "container", "location"]
    list_display = ["container_name", "location", "datetime"]

    @admin.display(ordering='container__name', description='Container')
    def container_name(self, obj):
        return obj.container.name


admin.site.register(Relocation, RelocationAdmin)

class ResoilAdmin(admin.ModelAdmin):
    fields = ["datetime", "container", "type"]
    list_display = ["type", "datetime"]


admin.site.register(Resoil, ResoilAdmin)

class SpeciesAdmin(admin.ModelAdmin):
    fields = ["common_name", "latin_binomial"]
    list_display = ["common_name", "latin_binomial"]


admin.site.register(Species, SpeciesAdmin)

class PlantAdmin(admin.ModelAdmin):
    fields = ["datetime", "name", "species", "supplier", "source", "parent", "container"]
    list_display = ["name", "datetime"]


admin.site.register(Plant, PlantAdmin)

class TransplantAdmin(admin.ModelAdmin):
    fields = ["datetime", "plant", "container"]
    list_display = ["plant_name", "container_name", "datetime"]

    @admin.display(ordering='plant__name', description='Plant')
    def plant_name(self, obj):
        return obj.plant.name

    @admin.display(ordering='container__name', description='Container')
    def container_name(self, obj):
        return obj.container.name


admin.site.register(Transplant, TransplantAdmin)

class ProduceAdmin(admin.ModelAdmin):
    fields = ["species", "name"]
    list_display = ["name"]


admin.site.register(Produce, ProduceAdmin)

class HarvestAdmin(admin.ModelAdmin):
    fields = ["datetime", "plant", "produce", "weight", "unit"]
    list_display = ["produce_name", "weight", "unit", "datetime"]

    @admin.display(ordering='produce__name', description='Produce')
    def produce_name(self, obj):
        return obj.produce.name


admin.site.register(Harvest, HarvestAdmin)

class ObservationAdmin(admin.ModelAdmin):
    fields = ["datetime", "plant", "text"]
    list_display = ["plant_name", "text", "datetime"]

    @admin.display(ordering='plant__name', description='Plant')
    def plant_name(self, obj):
        return obj.plant.name


admin.site.register(Observation, ObservationAdmin)

class WaterAdmin(admin.ModelAdmin):
    fields = ["datetime", "plant", "amount", "unit"]
    list_display = ["plant_name", "amount", "unit", "datetime"]

    @admin.display(ordering='plant__name', description='Plant')
    def plant_name(self, obj):
        return obj.plant.name


admin.site.register(Water, WaterAdmin)

class PruneAdmin(admin.ModelAdmin):
    fields = ["datetime", "plant", "text"]
    list_display = ["plant_name", "text", "datetime"]

    @admin.display(ordering='plant__name', description='Plant')
    def plant_name(self, obj):
        return obj.plant.name


admin.site.register(Prune, PruneAdmin)

class FertilizeAdmin(admin.ModelAdmin):
    fields = ["datetime", "plant", "type", "amount", "unit"]
    list_display = ["plant_name", "type", "amount", "unit", "datetime"]

    @admin.display(ordering='plant__name', description='Plant')
    def plant_name(self, obj):
        return obj.plant.name


admin.site.register(Fertilize, FertilizeAdmin)

class MulchAdmin(admin.ModelAdmin):
    fields = ["datetime", "plant", "type"]
    list_display = ["plant_name", "type", "datetime"]

    @admin.display(ordering='plant__name', description='Plant')
    def plant_name(self, obj):
        return obj.plant.name


admin.site.register(Mulch, MulchAdmin)

class DeathAdmin(admin.ModelAdmin):
    fields = ["datetime", "plant"]
    list_display = ["plant_name", "datetime"]

    @admin.display(ordering='plant__name', description='Plant')
    def plant_name(self, obj):
        return obj.plant.name


admin.site.register(Death, DeathAdmin)

