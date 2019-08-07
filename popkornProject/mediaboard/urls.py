from django.urls import path
from .import views

urlpatterns = [
    path('',views.media,name='media'),
    path('create',views.create,name='media_create'),
    path('delete/<int:board_id>',views.delete,name='media_delete'),
    path('edit/<int:board_id>',views.edit,name='media_edit'),
    path('update/<int:board_id>',views.update,name='media_update'),
]