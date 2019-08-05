from django.contrib import admin
from .models import Posting
from .models import PostingComment

#models에서 공지사항 데이터베이스 import
from .models import Notice

#관리자에서 Notice(공지사항) 등록 가능
admin.site.register(Notice)
admin.site.register(Posting)
admin.site.register(PostingComment)