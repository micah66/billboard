from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=75)
    body = forms.CharField(max_length=1000)
    author = forms.CharField(max_length=40)
