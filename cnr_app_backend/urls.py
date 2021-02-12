"""cnr_app_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from contact.api import ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('posts.urls')),
    path('eCommerce/', include('eCommerce.urls')),
    path('eHealth/', include('health.urls')),
    path('about/', include('AboutPerson.urls')),
    path('contact/', ContactView.as_view()),
    path('events/', include('event.urls')),
    path('eVehicle/',include('vehicle.urls')),
    path('employment/',include('employment.urls')),
]
