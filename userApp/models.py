from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from mainApp.models import Branch


class Role(models.Model):
    name = models.CharField(max_length=20)
    fixed_salary = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    min_customers = models.PositiveSmallIntegerField(blank=True, null=True)
    to_min = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    from_min = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    point = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    point = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    boss = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='bosses')

    def __str__(self):
        return f"{self.role}: {self.username}"
