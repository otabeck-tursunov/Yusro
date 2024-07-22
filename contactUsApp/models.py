from django.db import models


class Newsletter(models.Model):
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number


class Lid(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
