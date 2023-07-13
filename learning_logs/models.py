from django.db import models

'''Create models to store data used in the app'''
# Create your models here.


class Topic(models.Model):
    '''A topic the user is learning about'''

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''return string representation of the model'''
        return self.text


class Entry(models.Model):
    '''Something specific learned about a topic'''

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Store extra info for managing a model'''
        verbose_name_plural = 'entries'

    def __str__(self):
        '''return string representation of the model'''
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."
