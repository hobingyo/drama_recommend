from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/', views.article, name='article'),
    path('article/<int:id>', views.detail_article, name='detail-article'),
    path('article/comment/<int:id>', views.write_comment, name='write-comment'),
]
