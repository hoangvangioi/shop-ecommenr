from collections import defaultdict
from django import forms
from .models import *


class SearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = ' Tìm kiếm bài viết '
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder': ' Tìm kiếm . . . ',})


class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
            }))

    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
            }))
        
    subject = forms.CharField(max_length=255, required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control'
            }))

    message = forms.CharField(max_length=1000, required=True, 
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')