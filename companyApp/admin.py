from django.contrib import admin
from .models import *

admin.site.register([CompanyInformation, Member, Service, Comfort, Partnership, Testimonial, Question])
