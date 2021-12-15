from django import forms
from .models import Comment
from django.urls import reverse

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        