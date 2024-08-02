from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoriesListAPIView.as_view()),

    path('articles/', ArticleListAPIView.as_view()),
    path('articles/<int:article_id>/', ArticleRetrieveAPIView.as_view()),

    path('comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:comment_id>/', CommentRetrieveAPIView.as_view()),

    # path('tags/', TagsListAPIView.as_view()),
    path('tags/<int:tag_id>/', TagRetrieveAPIView.as_view()),

]
