#!/usr/bin/env python

''' Use models.py to define the models for the project. These models define how
    to work with the data that will be stored in the app. '''


from django.db import models


# Create your models here.


class Topic(models.Model):
    ''' A topic the user is learning about. '''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return a string representation of the model'''
        return self.text



class Entry(models.Model):
    '''Used to input somehting specific learned about
    a topic'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''This class holds extra information for managing a model'''
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Return a string representation of the model'''
        return f"{self.text[:50]}..."
        