#!/usr/bin/env python


from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
