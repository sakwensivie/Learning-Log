from django.contrib import admin

'''Manages admin previleges'''
# Register your models here.


from learning_logs.models import Topic
from learning_logs.models import Entry


admin.site.register(Topic)
admin.site.register(Entry)
