from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 메인
    path('article/', views.article, name='article'), # GET : 게시물 리스팅 / POST : 게시물 등록
    path('article/<int:id>', views.detail_article, name='detail-article'), # 게시물 상세 페이지
    path('article/comment/<int:id>', views.write_comment, name='write-comment'), # 댓글 등록
    path('article/comment/delete/<int:id>', views.delete_comment, name='delete-comment'), # 댓글 삭제
    path('article/like/<int:id>', views.like, name='like'), # 찜하기
    path('like/', views.like_listing, name='like_listing'), # 찜한 페이지 리스팅
    path('search/', views.search, name='search'), # 검색 페이지 리스팅
]
