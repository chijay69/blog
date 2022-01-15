from django import forms
from .models import Comment

# your form goes here

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    to = forms.EmailField()
    email = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()
