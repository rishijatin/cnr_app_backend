from django.urls import path
from .api import CategoryView, DoctorListView, DoctorDetailView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('category=<int:category_id>/', DoctorListView.as_view()),
    path('<int:doctor_id>/', DoctorDetailView.as_view()),
]
