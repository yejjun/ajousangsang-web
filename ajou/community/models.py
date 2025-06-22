# community/models.py
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200) # 질문 제목
    content = models.TextField() # 질문 내용
    created_at = models.DateTimeField(auto_now_add=True) # 작성일시 (자동으로 현재 시간 기록)

    def __str__(self):
        return self.title # 관리자 페이지 등에서 객체를 제목으로 표시

    class Meta:
        ordering = ['-created_at'] # 최신 글이 위에 오도록 정렬

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title