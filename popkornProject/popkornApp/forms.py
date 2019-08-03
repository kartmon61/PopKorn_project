from django import forms
from .models import Posting

from ckeditor_uploader.widgets import CKEditorUploadingWidget
 

class Communitycreate(forms.ModelForm):
    class Meta:
        model = Posting
 
        fields = ['title', 'created_at', 'content'] 

widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }