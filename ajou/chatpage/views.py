from django.shortcuts import render

# chat_view 함수가 없거나 이름이 다르면 이 오류가 발생합니다.
def chat_view(request):
    return render(request, 'chatpage/chatpage.html')

from django.shortcuts import render
from rest_framework.views import APIView

