from django.db import models

from mainApp.models import Nationality
from userApp.models import User


class Tour(models.Model):
    name = models.CharField(max_length=255)
    members_count = models.PositiveSmallIntegerField(blank=True, null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + str(self.members_count)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    passport_serial_letter = models.CharField(max_length=2, blank=True, null=True)
    passport_serial_number = models.CharField(max_length=7, blank=True, null=True)
    passport_start_date = models.DateField(blank=True, null=True)
    passport_end_date = models.DateField(blank=True, null=True)
    passport_image = models.ImageField(upload_to='passports/', blank=True, null=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, blank=True, null=True)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


