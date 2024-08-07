from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Yusro Website API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="otabecktursunov@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('main/', include('mainApp.urls')),
    path('users/', include('userApp.urls')),
    path('company/', include('companyApp.urls')),
    path('contact-us/', include('contactUsApp.urls')),
    path('record/', include('recordApp.urls')),
    path('post/', include('articleApp.urls')),
    path('travel/', include('travelApp.urls')),
    path('landing-admin/', include('LANDING.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
