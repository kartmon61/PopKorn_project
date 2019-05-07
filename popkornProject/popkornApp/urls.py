from django.urls import path
from .import views

urlpatterns = [
    # <임시처리>
    # // 첫화면 index 화면이 보이게 설정
    # /header로 링크 들어가면 header 화면이 보이게 설정
    # /footer로 링크 들어가면 footer 화면이 보이게 설정
    # /news로 링크 들어가면 news 화면이 보이게 설정
    # /chart로 링크 들어가면 chart 화면이 보이게 설정
    # /media로 링크 들어가면 media 화면이 보이게 설정
    # /calendar로 링크 들어가면 calendar 화면이 보이게 설정
    # /community로 링크 들어가면 community 화면이 보이게 설정
    
    path('',views.index,name='index'),
    path('header',views.header,name='header'),
    path('footer',views.footer,name='footer'),
    path('news',views.news,name='news'),
    path('chart',views.chart,name='chart'),
    path('media',views.media,name='media'),
    path('calendar',views.calendar,name='calendar'),
    path('community',views.community,name='community'),
]