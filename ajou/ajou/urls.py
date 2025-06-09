"""
URL configuration for ajou project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from django.urls import path, include
from .views import Main
from django.views.generic import TemplateView

urlpatterns = [
    path('', Main.as_view(),name='main_page'),
    path('chatpage/', include('chatpage.urls')),
    path('login/', include('login.urls')),
    path('sign_up/', include('sign_up.urls')),
    path('myprofile/', include('myprofile.urls')),
    path('notice/', include('notice.urls')),
    path('community/', include('community.urls')),
    path('contest/', include('contest.urls')),


]
