from django.urls import path
from . import views

urlpatterns = [

    path('', views.contest_view, name='contest_page'),
]