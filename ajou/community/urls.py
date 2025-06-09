from django.urls import path
from . import views

urlpatterns = [

    path('', views.community_view, name='community_page'),
    path('ask/', views.ask_view, name='ask_page'),
    path('together/', views.together_view, name='together_page'),
    path('ask/submit/', views.ask_question_submit_view, name='ask_question_submit'),
]