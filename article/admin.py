from django.contrib import admin
from .models import ArticleModel, ArticleComment, UserLike
# Register your models here.

admin.site.register(ArticleModel)
admin.site.register(ArticleComment)
admin.site.register(UserLike)