from django import forms
from .models import Neighborhood, Post, Business
from django.contrib.auth.models import User

# class NewArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         exclude = ['editor', 'pub_date']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }