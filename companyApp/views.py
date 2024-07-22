from drf_yasg.utils import swagger_auto_schema
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


class MembersListAPIView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ServicesListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ComfortsListAPIView(ListAPIView):
    queryset = Comfort.objects.all()
    serializer_class = ComfortSerializer


class PartnerShipsListAPIView(ListAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer


class TestimonialsListAPIView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    @swagger_auto_schema(

    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Testimonial.objects.all()

        order_by = self.request.query_params.get('order_by', None)
        if order_by is not None:
            if order_by.lower() == 'created_at':
                queryset = queryset.order_by('created_at')
            elif order_by.lower() == '-created_at':
                queryset = queryset.order_by('-created_at')
        return queryset


class QuestionsListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class DiscussionsListAPIView(ListAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
