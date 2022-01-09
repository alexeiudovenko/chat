from django.db import models

from datetime import datetime


class Topic(models.Model):
    topic_name = models.CharField(max_length=50, verbose_name='Topic of discussion')

    def __str__(self):
        return self.topic_name

class Message(models.Model):
    topic_message = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=50, verbose_name='Sender`s name')
    text = models.TextField(verbose_name='Text')
    date_time = models.DateTimeField(verbose_name='Date and time', default=datetime.now())
    anonymous = models.BooleanField(verbose_name='Anon', default=False)

    def __str__(self):
        return self.text

class DelayedMessages(models.Model):
    topic_message = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=50, verbose_name='Sender`s name')
    text = models.TextField(verbose_name='Text')
    date_time = models.DateTimeField(verbose_name='Date and time', default=datetime.now())
    anonymous = models.BooleanField(verbose_name='Anon', default=False)

    def __str__(self):
        return self.text