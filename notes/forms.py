# vi notes/forms.py

from django import forms
from .models import Category, Note

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['text']
        labels = {'text': ''}

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        labels = {'text': 'Note:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
