from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'category', 'image', 'content']
        labels = {
            'title':'Story title', 
            'category':'Choose a category', 
            'image':'Image URL',
            'content':'Story content'
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields =['content']
        
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control rounded',
        'placeholder':'Leave a comment here!',
        'rows':4,
        'cols':50
    }))
    

    

       #field_classes = {
       #    'title':'rounded', 
       #    'category':'rounded', 
       #    'image':'rounded',
       #    'content':'rounded'
       #}


        #widgets = {
        #    'pub_date': forms.DateInput(
        #        format='%m/%d/%Y %H:%M:%S',
        #        attrs={
        #            'class': 'form-control',
        #            'placeholder': 'Select a date',
        #            'type': 'date'
        #        }
        #    )
        #}