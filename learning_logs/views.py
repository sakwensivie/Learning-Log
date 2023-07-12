#!/usr/bin/env python

'''Accepts data from a request and uses it to generate a page 
for the user to see'''
from django.shortcuts import render

# Create your views here.
def index(request):
    '''The home page for learning log'''
    return render(request, 'learning_logs/index.html')
