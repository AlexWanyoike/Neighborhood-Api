from django import forms
from .models import Neighborhood, Post, Business 
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['username', 'neighbourhood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'post']