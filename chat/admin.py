from django.contrib import admin

from .models import Topic, Message, DelayedMessages

admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(DelayedMessages)
