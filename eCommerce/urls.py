from django.urls import path
from .api import ItemListView,ItemDetailView,CategoryView

urlpatterns = [
    path('',CategoryView.as_view()),
    path('category=<int:category_id>/',ItemListView.as_view()),
    path('<int:item_id>/',ItemDetailView.as_view()),
]