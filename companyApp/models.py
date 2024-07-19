from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class CompanyInformation(models.Model):
    site_logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    visas_count = models.IntegerField(default=0)
    travelers_count = models.IntegerField(default=0)
    instagram_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)
    telegram_admin = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Company Information"


class Member(models.Model):
    full_name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='team-members/', null=True, blank=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo__path = models.ImageField(upload_to='service_logos/', null=True, blank=True)
    background_path = models.ImageField(upload_to='service_backgrounds/', null=True, blank=True)

    def __str__(self):
        return self.name


class Comfort(models.Model):
    description = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to='comforts/', null=True, blank=True)

    def __str__(self):
        return self.description


class Partnership(models.Model):
    name = models.CharField(max_length=100)
    logo_path = models.ImageField(upload_to='partnership_logos/', null=True, blank=True)
    site_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    full_name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    rate = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    conclusion = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
