from django.shortcuts import render

#관리자 공지사항 Notice 추가 (사용가능)
from .models import Notice

# Create your views here.
def header(request):
    return render(request,'header.html')

def index(request):
    return render(request,'index.html')

def footer(request):
    return render(request,'footer.html')
