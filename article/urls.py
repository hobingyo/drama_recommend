from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/', views.article, name='article'),
    path('article/<int:id>', views.detail_article, name='detail-article'),
    path('article/comment/<int:id>', views.write_comment, name='write-comment'),
    path('article/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
    path('article/like/<int:id>', views.like, name='like'),
    path('like/', views.like_listing, name='like_listing'),
    path('search/', views.search, name='search'),
]
