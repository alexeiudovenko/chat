from celery import shared_task

from .models import DelayedMessages, Message

from datetime import datetime

from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync



@shared_task
def send_delayed_messages():
    delayed_message = DelayedMessages.objects.order_by('date_time').first()
    
    if (delayed_message.date_time.date() <= datetime.now().date()) and (delayed_message.date_time.time() <= datetime.now().time()):
        new_message = Message.objects.create(
                topic_message=delayed_message.topic_message,
                sender_name=delayed_message.sender_name,
                text=delayed_message.text,
                date_time=delayed_message.date_time,
                anonymous=delayed_message.anonymous,
            )

        delayed_message.delete()

        data = {
            'sender_name' : 'Anonymous' if new_message.anonymous else new_message.sender_name,
            'text' : new_message.text,
            'date_time' : new_message.date_time.strftime("%b, %d, %Y %I:%M %p"),
        }

        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            f'chat_{new_message.topic_message.id}',
            {
                'type': 'chat_message',
                'message': data
            }
        )


    return new_message.sender_name
    