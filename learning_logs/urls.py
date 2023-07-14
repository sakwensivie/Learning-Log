'''Defines URL patterns for learning_logs.'''


from django.urls import path, include
from . import views

urlpatterns = [
    # Home page
    path('', views.index)
]