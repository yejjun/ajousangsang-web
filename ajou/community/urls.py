from django.urls import path
from . import views

urlpatterns = [

    path('', views.community_view, name='community_page'),
    path('ask/', views.ask_view, name='ask_page'),
    path('ask/submit/', views.ask_question_submit_view, name='ask_question_submit'),
    path('', views.community_view, name='community_page'),
    path('ask/', views.ask_view, name='ask_page'),
    path('ask/submit/', views.ask_question_submit_view, name='ask_question_submit'),

    # 같이해요 게시판
    path('together/', views.together_view, name='together_page'),
    path('together/<int:pk>/', views.together_detail_view, name='together_detail'),
    path('together/write/', views.together_write_view, name='together_write'),
]