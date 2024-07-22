from django.contrib import admin
from .models import *

admin.site.register([TourType, Place, TourPack, PackInclude])
