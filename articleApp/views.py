from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *

from .serializers import *
from .models import *


class CategoriesListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='order_by',
                description='Order by title, articles_amount',
                type=openapi.TYPE_STRING,
                in_=openapi.IN_QUERY,
                enum=['title', '-title', 'articles_amount', '-articles_amount'],
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Category.objects.all()

        order_by = self.request.query_params.get('order_by')
        if order_by is not None:
            if order_by.lower() == 'title':
                queryset = queryset.order_by('title')
            elif order_by.lower() == '-title':
                queryset = queryset.order_by('-title')

            if order_by.lower() == 'articles_amount':
                queryset = queryset.order_by('articles_amount')
            elif order_by.lower() == '-articles_amount':
                queryset = queryset.order_by('-articles_amount')
        return queryset


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = PageNumberPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='page_size',
                type=openapi.TYPE_INTEGER,
                description='Number of items per page',
                in_=openapi.IN_QUERY,
            ),
            openapi.Parameter(
                name='search',
                type=openapi.TYPE_STRING,
                description='Search by title, intro_text',
                in_=openapi.IN_QUERY,
            ),
            openapi.Parameter(
                name='author',
                type=openapi.TYPE_STRING,
                description='Filter by Author',
                in_=openapi.IN_QUERY,
            ),
            openapi.Parameter(
                name='category_id',
                type=openapi.TYPE_INTEGER,
                description='Filter by Category ID',
                in_=openapi.IN_QUERY,
            ),
            openapi.Parameter(
                name='tag_id',
                type=openapi.TYPE_INTEGER,
                description='Filter by Tag ID',
                in_=openapi.IN_QUERY,
            ),
            openapi.Parameter(
                name='order_by',
                type=openapi.TYPE_STRING,
                description='Order by title, views, created_at',
                in_=openapi.IN_QUERY,
                enum=['title', '-title', 'views', '-views', 'created_at', '-created_at'],
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Article.objects.all()

        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(intro_text__icontains=search)
            )

        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author__icontains=author)

        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            get_object_or_404(Category, pk=category_id)
            queryset = queryset.filter(category_id=category_id)

        order_by = self.request.query_params.get('order_by')
        if order_by is not None:
            queryset = queryset.order_by(order_by)

        tag_id = self.request.query_params.get('tag_id')
        if tag_id is not None:
            get_object_or_404(Tag, pk=tag_id)
            article_ids = ArticleTag.objects.filter(tag_id=tag_id).values_list('article_id', flat=True)
            queryset = queryset.filter(id__in=article_ids)

        page_size = self.request.query_params.get('page_size')
        if page_size:
            self.pagination_class.page_size = int(page_size)
        return queryset


class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_object(self):
        article = get_object_or_404(Article, pk=self.kwargs['article_id'])
        article.views += 1
        article.save()
        return article


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='article_id',
                type=openapi.TYPE_INTEGER,
                description='Filter by Article ID',
                in_=openapi.IN_QUERY,
            ),
            openapi.Parameter(
                name='order_by',
                type=openapi.TYPE_STRING,
                description='Order by created_at',
                in_=openapi.IN_QUERY,
                enum=['created_at', '-created_at'],
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Comment.objects.all()

        article_id = self.request.query_params.get('article_id')
        if article_id is not None:
            get_object_or_404(Article, pk=article_id)
            queryset = queryset.filter(article_id=article_id)

        order_by = self.request.query_params.get('order_by')
        if order_by is not None:
            if order_by.lower() == 'created_at':
                queryset = queryset.order_by('created_at')
            elif order_by.lower() == '-created_at':
                queryset = queryset.order_by('-created_at')

        return queryset


class CommentRetrieveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_object(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['comment_id'])
        return comment


class TagsListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                type=openapi.TYPE_STRING,
                description='Search by name',
                in_=openapi.IN_QUERY,
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TagRetrieveAPIView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_object(self):
        tag = get_object_or_404(Tag, pk=self.kwargs['tag_id'])
        return tag
