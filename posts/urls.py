from django.urls import path
from .api import ListCategories, BlogPostList, BlogPostDetail

urlpatterns = [
    path('get/', ListCategories.as_view()),
    path('get/category=<int:category_id>/', BlogPostList.as_view()),
    path('get/<int:item_id>/', BlogPostDetail.as_view()),

]
