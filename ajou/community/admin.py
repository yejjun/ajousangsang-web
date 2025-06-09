# community/admin.py
from django.contrib import admin
from .models import Question # 위에서 정의한 Question 모델 임포트

admin.site.register(Question)
