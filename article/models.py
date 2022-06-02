from django.db import models
from user.models import UserModel
# Create your models here.

class ArticleModel(models.Model):
    class Meta:
        db_table = "article"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    synopsis = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    tags = models.CharField(max_length=256)
    cast = models.CharField(max_length=256)
    rating = models.IntegerField()
    aired_date = models.DateTimeField()
    episode = models.IntegerField()
    aged = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)