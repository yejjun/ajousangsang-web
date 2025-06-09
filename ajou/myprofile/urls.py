from django.urls import path
from . import views

urlpatterns = [

    path('', views.myprofile_view, name='myprofile_page'),
]