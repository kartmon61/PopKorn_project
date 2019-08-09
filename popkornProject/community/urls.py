from django.urls import path
from .import views

urlpatterns = [
    path('',views.community,name=''),
    path('new',views.communitynew,name='new'),
    # path('create',views.communitycreate,name='create'),
    path('show/<int:post_id>',views.communityshow,name='show'),
    path('edit/<int:post_id>',views.communityedit,name='edit'),
    path('update/<int:post_id>',views.communityupdate,name='update'),
    path('delete/<int:post_id>',views.communitydelete,name='delete'),
    path('commentcreate/<int:post_id>',views.commentcreate,name='comentcreate'),
    path('commentdelete/<int:post_id>/<int:comment_id>',views.commentdelete,name='comentdelete'),
]