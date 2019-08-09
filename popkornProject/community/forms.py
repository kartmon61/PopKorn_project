from django import forms
from .models import Posting
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommunityCreate(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['title','content']
        
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control input_', 'style': 'width: 69%; display:inline; font-size:1em;', 'placeholder': 'TITLE'}
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }