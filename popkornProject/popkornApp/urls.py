from django.urls import path
from .import views

urlpatterns = [
    # <임시처리>
    # // 첫화면 index 화면이 보이게 설정
    # /header로 링크 들어가면 header 화면이 보이게 설정
    # /footer로 링크 들어가면 footer 화면이 보이게 설정
    
    path('',views.index,name='index'),
    path('header',views.header,name='header'),
    path('footer',views.footer,name='footer'),
]