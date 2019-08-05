#models import
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

#관리자 글 생성 --> 공지사항 글 포맷 설정 
class Notice(models.Model):
    title = models.CharField(max_length=200) #타이틀 설정
    created_at = models.DateTimeField(auto_now_add=True) #현재시각 설정
    content = RichTextUploadingField() #내용 설정


class Posting(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=True,null=True,default=1)
    content = RichTextUploadingField()


class PostingComment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    posting = models.ForeignKey(Posting,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=True,null=True,default=1)

