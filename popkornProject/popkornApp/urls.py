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
    path('news',views.news,name='news'),
    path('chart',views.chart,name='chart'),
    path('melon',views.chartmelon,name='chartmelon'),
    path('gini',views.chartgini,name='chartgini'),
    path('mnet',views.chartmnet,name='chartmnet'),
    path('buks',views.chartbuks,name='chartbuks'),
    path('media',views.media,name='media'),
    path('calendar',views.calendar,name='calendar'),
    path('community',views.community,name='community'),
    path('community/new',views.communitynew,name='communitynew'),
    path('community/create',views.communitycreate,name='communitycreate'),
    path('community/show/<int:post_id>',views.communityshow,name='communityshow'),
    path('community/edit/<int:post_id>',views.communityedit,name='communityedit'),
    path('community/update/<int:post_id>',views.communityupdate,name='communityupdate'),
    path('community/delete/<int:post_id>',views.communitydelete,name='communitydelete'),
    path('community/comentcreate/<int:post_id>',views.comentcreate,name='comentcreate'),
    path('community/comentdelete/<int:post_id>/<int:coment_id>',views.comentdelete,name='comentdelete'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'), 

]