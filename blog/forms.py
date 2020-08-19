from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'post_slug',
            'text'
        ]
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control border-0 shadow-sm',
                'placeholder': 'Tulis komentar disini...',
                'cols': '100%', 
                'rows': 3
            }),
            'post_slug': forms.HiddenInput()
        }
