from django.urls import path
from .api import CategoryView, FunctionDetailView, FunctionListView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('category=<int:category_id>/', FunctionListView.as_view()),
    path('<int:item_id>/', FunctionDetailView.as_view()),
]
