from rest_framework import serializers
from .models import *


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    def to_representation(self, instance):
        place = super(PlaceSerializer, self).to_representation(instance)

        tour_packs = TourPack.objects.filter(place=instance)
        tour_packs_serializer = TourPackSerializer(tour_packs, many=True)

        place.update(
            {
                'tour_packs': tour_packs_serializer.data
            }
        )
        return place


class TourPackCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPack
        fields = '__all__'


class TourPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPack
        fields = '__all__'

    def to_representation(self, instance):
        tour_pack = super(TourPackSerializer, self).to_representation(instance)

        pack_includes = PackInclude.objects.filter(tour_pack=instance)
        pack_includes_serializer = PackIncludeCascadeSerializer(pack_includes, many=True)

        tour_pack.update(
            {
                'pack_includes': pack_includes_serializer.data
            }
        )
        return tour_pack


class PackIncludeCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackInclude
        fields = '__all__'
