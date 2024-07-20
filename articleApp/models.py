from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to="categories/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    articles_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    intro_text = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to="articles/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.article.title[:30]}: {self.tag.name}"
