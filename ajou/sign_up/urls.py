from django.urls import path
from . import views

urlpatterns = [

    path('', views.sign_up_view, name='sign_up_page'),
]