from django.urls import path
from .api import CategoryView, NewsListView, NewsDetailView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('category=<int:category_id>/', NewsListView.as_view()),
    path('<int:article_id>/',NewsDetailView.as_view())
]