from django.db import models
from user.models import UserModel
from taggit.managers import TaggableManager

# Create your models here.

class ArticleModel(models.Model):
    class Meta:
        db_table = "article"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    poster = models.FileField(upload_to="Uploaded_Files/")
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

# 데이터베이스 드라마 리스트 모델
class ArticleList(models.Model):
    class Meta:
        db_table = "article_list"

    title = models.CharField(max_length=256)
    synopsis = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)
    cast = models.CharField(max_length=256)
    rating = models.FloatField()
    episode = models.IntegerField()
    aired_date = models.CharField(max_length=256)
    aged = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ArticleComment(models.Model):
    class Meta:
        db_table = "comment"

    article = models.ForeignKey(ArticleList, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserLike(models.Model):
    class Meta:
        db_table = "like"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleList, on_delete=models.CASCADE)



# 추천 드라마
class ArticleRecomm(models.Model):
    class Meta:
        db_table = "article_recomm"

    title = models.CharField(max_length=256)
    synopsis = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)
    cast = models.CharField(max_length=256)
    rating = models.FloatField()
    episode = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)