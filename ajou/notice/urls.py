from django.urls import path
from . import views

urlpatterns = [

    path('', views.notice_view, name='notice_page'),
]