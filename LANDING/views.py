from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.views import APIView

from contactUsApp.serializers import *
from contactUsApp.models import *

from travelApp.serializers import *
from travelApp.models import *

from userApp.serializers import *
from userApp.models import *

from articleApp.serializers import *
from articleApp.models import Category

from companyApp.serializers import *
from companyApp.models import *


# ------------- Company Information ----------------

class MemberListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ServiceListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ComfortListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Comfort.objects.all()
    serializer_class = ComfortSerializer


class ComfortRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Comfort.objects.all()
    serializer_class = ComfortSerializer


class PartnershipListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer


class PartnershipRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer


class TestimonialListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class TestimonialRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class QuestionListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# ------------- Article Posts ----------------

class CategoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TagListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleTagListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Article.objects.all()
    serializer_class = ArticleTagSerializer


class ArticleTagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Article.objects.all()
    serializer_class = ArticleTagSerializer


# ------------- Contact ----------------

class DiscussionListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class DisscussionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer


class NewsletterListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class NewsletterRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class LidListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Lid.objects.all()
    serializer_class = LidSerializer


class LidRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Lid.objects.all()
    serializer_class = LidSerializer


# ------------- Travel ----------------


class TourTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = TourType.objects.all()
    serializer_class = TourTypeSerializer


class TourTypeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = TourType.objects.all()
    serializer_class = TourTypeSerializer


class PlaceListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class TourPackListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = TourPack.objects.all()
    serializer_class = TourPackSerializer


class TourPackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = TourPack.objects.all()
    serializer_class = TourPackSerializer


class PackIncludeListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = PackInclude.objects.all()
    serializer_class = PackIncludeSerializer


class PackIncludeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = PackInclude.objects.all()
    serializer_class = PackIncludeSerializer


# --------------- User, Role ---------------------

class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserUpdateAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user
