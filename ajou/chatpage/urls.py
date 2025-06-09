from django.urls import path
from . import views # chatpage 앱의 views.py를 임포트

urlpatterns = [
    # path('', views.ChatView.as_view(), name='chat_page'), # 클래스 기반 뷰를 사용한다면
    path('', views.chat_view, name='chat_page'),
]