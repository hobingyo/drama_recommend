from django.db import models
from user.models import UserModel
from taggit.managers import TaggableManager

# Create your models here.

class ArticleModel(models.Model):
    class Meta:
        db_table = "article"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    poster = models.CharField(max_length=256, default='')
    synopsis = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)
    cast = models.CharField(max_length=256)
    rating = models.FloatField()
    aired_date = models.DateTimeField()
    episode = models.IntegerField()
    aged = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ArticleComment(models.Model):
    class Meta:
        db_table = "comment"

    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserLike(models.Model):
    class Meta:
        db_table = "like"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
