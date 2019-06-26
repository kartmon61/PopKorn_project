#models import
from django.db import models

#관리자 글 생성 --> 공지사항 글 포맷 설정 
class Notice(models.Model):
    title = models.CharField(max_length=200) #타이틀 설정
    created_at = models.DateTimeField(auto_now_add=True) #현재시각 설정
    content = models.TextField() #내용 설정


class Posting(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class PostingComent(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posting,on_delete=models.CASCADE)
