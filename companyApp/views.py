from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.views import APIView

from .serializers import *
from .models import *


class CompanyInformationAPIView(APIView):
    def get(self, request):
        information = CompanyInformation.objects.last()
        serializer = CompanyInformationSerializer(information)
        return Response(serializer.data)
