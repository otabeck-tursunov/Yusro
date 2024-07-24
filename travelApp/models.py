from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TourType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image_path = models.ImageField(upload_to='places/', blank=True, null=True)
    important = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    tour_type = models.ForeignKey(TourType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class TourPack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    background_image_path = models.ImageField(upload_to="tour-packs/", blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name + ": " + self.name


class PackInclude(models.Model):
    text = models.TextField()
    tour_pack = models.ForeignKey(TourPack, on_delete=models.CASCADE)

    def __str__(self):
        return self.tour_pack.name + " - " + self.text[:30]
