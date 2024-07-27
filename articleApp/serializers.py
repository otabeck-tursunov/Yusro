from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        category = super(CategorySerializer, self).to_representation(instance)

        articles_amount = instance.article_set.count()
        category.update(
            {
                'articles_amount': articles_amount
            }
        )
        return category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        article = super(ArticleSerializer, self).to_representation(instance)

        tags = Tag.objects.filter(id__in=ArticleTag.objects.filter(article=instance).values_list('id', flat=True))
        tags_serializer = TagSerializer(tags, many=True)

        comments = Comment.objects.filter(article=instance)
        comments_serializer = CommentSerializer(comments, many=True)

        article.update(
            {
                'tags': tags_serializer.data,
                'comments': comments_serializer.data
            }
        )
        return article


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = '__all__'
