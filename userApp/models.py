from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from mainApp.models import Branch


class Role(models.Model):
    name = models.CharField(max_length=20, unique=True)
    fixed_salary = models.FloatField(validators=[MinValueValidator(0.0)])
    min_customers = models.PositiveSmallIntegerField()




class User(AbstractUser):
    ROLE_CHOICES = (
        ('Agent', 'Agent'),
        ('Ashir', 'Ashir'),
        ('Kurator', 'Kurator'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    point = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.role}: {self.username}"
