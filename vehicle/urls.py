from django.urls import path
from .api import CategoryView, DetailsView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('category=<int:category_id>/', DetailsView.as_view()),
]