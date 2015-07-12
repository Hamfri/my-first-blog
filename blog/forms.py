from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title =  forms.CharField(error_messages={'required': 'Your post should have a title'})
    text = forms.CharField(widget=forms.Textarea, error_messages={'required': 'The text field must not be blank'})
    class Meta:
        model = Post
        fields = ('title','text')