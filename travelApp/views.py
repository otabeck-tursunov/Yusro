from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import *
from rest_framework.views import APIView

from .serializers import *
from .models import *


class PlacesListAPIView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='tour_type_id',
                description='Filter by Tour Type ID',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                name='order_by',
                description='Order by Important',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['important']
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Place.objects.all()

        tour_type_id = self.request.query_params.get('tour_type_id', None)
        if tour_type_id is not None:
            get_object_or_404(TourType, id=tour_type_id)
            queryset = queryset.filter(tour_type__id=tour_type_id)

        order_by = self.request.query_params.get('order_by', None)
        if order_by is not None:
            queryset = queryset.order_by(order_by)

        return queryset


class TourPacksListAPIView(ListAPIView):
    queryset = TourPack.objects.all()
    serializer_class = TourPackSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='place_id',
                description='Filter by Place ID',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                name='order_by',
                description='Order by Price',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['price']
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = TourPack.objects.all()

        place_id = self.request.query_params.get('place_id', None)
        if place_id is not None:
            get_object_or_404(Place, id=place_id)
            queryset = queryset.filter(place__id=place_id)

        order_by = self.request.query_params.get('order_by', None)
        if order_by is not None:
            queryset = queryset.order_by(order_by)
        return queryset


class TourPackRetrieveAPIView(RetrieveAPIView):
    queryset = TourPack.objects.all()
    serializer_class = TourPackSerializer

    def get_object(self):
        tour_pack = get_object_or_404(TourPack, pk=self.kwargs['tour_pack_id'])
        return tour_pack
