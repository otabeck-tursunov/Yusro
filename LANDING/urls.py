from django.urls import path
from .views import *

urlpatterns = [
    path('company/members/', MemberListCreateAPIView.as_view()),
    path('company/members/<int:pk>/', MemberRetrieveUpdateDestroyAPIView.as_view()),

    path('company/services/', ServiceListCreateAPIView.as_view()),
    path('company/services/<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view()),

    path('company/comforts/', ComfortListCreateAPIView.as_view()),
    path('company/comforts/<int:pk>/', ComfortRetrieveUpdateDestroyAPIView.as_view()),

    path('company/partnerships/', PartnershipListCreateAPIView.as_view()),
    path('company/partnerships/<int:pk>/', PartnershipRetrieveUpdateDestroyAPIView.as_view()),

    path('company/testimonials/', TestimonialListCreateAPIView.as_view()),
    path('company/testimonials/<int:pk>/', TestimonialRetrieveUpdateDestroyAPIView.as_view()),

    path('company/questions/', QuestionListCreateAPIView.as_view()),
    path('company/questions/<int:pk>/', QuestionRetrieveUpdateDestroyAPIView.as_view()),

    path('post/categories/', CategoryListCreateAPIView.as_view()),
    path('post/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),

    path('post/articles/', ArticleListCreateAPIView.as_view()),
    path('post/articles/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view()),

    path('post/comments/', CommentListCreateAPIView.as_view()),
    path('post/comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),

    path('post/tags/', TagListCreateAPIView.as_view()),
    path('post/tags/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view()),

    path('post/article-tags/', ArticleTagListCreateAPIView.as_view()),
    path('post/article-tags/<int:pk>/', ArticleTagRetrieveUpdateDestroyAPIView.as_view()),

    path('contact/discussion/', DiscussionListCreateAPIView.as_view()),
    path('contact/discussion/<int:pk>/', DisscussionRetrieveUpdateDestroyAPIView.as_view()),

    path('contact/newsletters/', NewsletterListCreateAPIView.as_view()),
    path('contact/newsletters/<int:pk>/', NewsletterRetrieveUpdateDestroyAPIView.as_view()),

    path('contact/lids/', LidListCreateAPIView.as_view()),
    path('contact/lids/<int:pk>/', LidRetrieveUpdateDestroyAPIView.as_view()),

    path('travel/tour-types/', TourTypeListCreateAPIView.as_view()),
    path('travel/tour-types/<int:pk>/', TourTypeRetrieveUpdateDestroyAPIView.as_view()),

    path('travel/places/', TourTypeListCreateAPIView.as_view()),
    path('travel/places/<int:pk>/', TourTypeRetrieveUpdateDestroyAPIView.as_view()),

    path('travel/tour-packs/', TourPackListCreateAPIView.as_view()),
    path('travel/tour-packs/<int:pk>/', TourPackRetrieveUpdateDestroyAPIView.as_view()),

    path('travel/pack-includes/', PackIncludeListCreateAPIView.as_view()),
    path('travel/pack-includes/<int:pk>/', PackIncludeRetrieveUpdateDestroyAPIView.as_view()),

    path('users/me/', UserRetrieveAPIView.as_view()),
    path('users/me/update/', UserUpdateAPIView.as_view())
]
