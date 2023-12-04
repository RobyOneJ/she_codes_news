from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'category', 'pub_date', 'image', 'content']
        labels = {
            'title':'Story title', 
            'category':'Choose a category', 
            'pub_date': 'Creation date',
            'image':'Image URL',
            'content':'Story content'
        }
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%Y %H:%M:%S',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }