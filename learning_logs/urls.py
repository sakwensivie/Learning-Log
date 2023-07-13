#!/usr/bin/env python

'''Defines url patters for learning_logs'''

from django.urls import path
# from django.conf.urls import url
from . import views


urlpatterns = [
    # Home page
    path(r'^$', views.index, name='index'),
]
