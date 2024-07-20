from django.db import models


class Nationality(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BranchCity(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch.name + " " + self.city.name
