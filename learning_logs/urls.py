'''Defines URL patterns for learning_logs.'''


from django.urls import path, include
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Topics page
    path('topics/', views.topics, name='topics'),

    # Detail page fo a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #page for adding new topics
    path('new_topic/', views.new_topic, name='new_topic'),

    # page for adding new entry
    path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    
]
