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

def news(request):
    return render(request,'news.html')

def chart(request):
    return render(request,'chart.html')

def media(request):
    return render(request,'media.html')

def calendar(request):
    return render(request,'calendar.html')

def community(request):
    return render(request,'community.html')
