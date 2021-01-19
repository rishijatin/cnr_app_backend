from django.urls import path
from .api import PersonInfo

urlpatterns = [
    path('<int:personId>/', PersonInfo.as_view()),
]
