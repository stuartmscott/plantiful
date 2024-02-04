from django.db import models
from django.utils.translation import gettext_lazy as _


class Unit(models.IntegerChoices):
    UNITLESS = 0, _("Unitless")
    GRAM = 1, _("Gram")
    LITRE = 2, _("Litre")
    KILOGRAM = 3, _("Kilogram")
    MILLILITRE = 4, _("Millilitre")


class Source(models.IntegerChoices):
    UNKNOWN = 0, _("Unknown")
    SEED = 1, _("Seed")
    SEEDLING = 2, _("Seedling")
    PROPAGATION = 3, _("Propagation")
    MATURE = 4, _("Mature")


class Container(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField(default=1)
    location = models.CharField(max_length=200)
    soil_type = models.CharField(max_length=200)


class Relocation(models.Model):
    datetime = models.DateTimeField("date of relocation")
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)


class Resoil(models.Model):
    datetime = models.DateTimeField("date of resoil")
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)


class Species(models.Model):
    common_name = models.CharField(max_length=200)
    latin_binomial = models.CharField(max_length=200)


class Plant(models.Model):
    datetime = models.DateTimeField("date of creation")
    name = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200, blank=True, null=True)
    source = models.IntegerField(
        choices=Source.choices,
        default=Source.UNKNOWN,
    )
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def source_name(self):
        return Source.choices[self.source][1]


class Transplant(models.Model):
    datetime = models.DateTimeField("date of transplanting")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)


class Produce(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Harvest(models.Model):
    datetime = models.DateTimeField("date of harvesting")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    unit = models.IntegerField(
        choices=Unit.choices,
        default=Unit.UNITLESS,
    )

    @property
    def unit_name(self):
        return Unit.choices[self.unit][1]


class Observation(models.Model):
    datetime = models.DateTimeField("date of observing")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    image = models.CharField(max_length=200)


class Water(models.Model):
    datetime = models.DateTimeField("date of watering")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    unit = models.IntegerField(
        choices=[(u.value, u.label) for u in [Unit.LITRE, Unit.MILLILITRE]],
        default=Unit.LITRE,
    )

    @property
    def unit_name(self):
        return Unit.choices[self.unit][1]


class Prune(models.Model):
    datetime = models.DateTimeField("date of pruning")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank=True, null=True)


class Fertilize(models.Model):
    datetime = models.DateTimeField("date of fertilizing")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    unit = models.IntegerField(
        choices=Unit.choices,
        default=Unit.UNITLESS,
    )

    @property
    def unit_name(self):
        return Unit.choices[self.unit][1]


class Mulch(models.Model):
    datetime = models.DateTimeField("date of mulching")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)


class Death(models.Model):
    datetime = models.DateTimeField("date of death")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
