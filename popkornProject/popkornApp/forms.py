from django import forms
from .models import Posting
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommunityCreate(forms.ModelForm):
    class Meta:
        model = Posting
 
        fields = ['title', 'author', 'content']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }