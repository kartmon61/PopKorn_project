from django.contrib import admin

#models에서 공지사항 데이터베이스 import
from .models import Notice

#관리자에서 Notice(공지사항) 등록 가능
admin.site.register(Notice)