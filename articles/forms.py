from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from . import models

class createArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']