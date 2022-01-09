from rest_framework import viewsets

from .serializers import TopicSerializer, MessageSerializer, UserSerializer, DelayedMessagesSerializer

from chat.models import Topic, Message, DelayedMessages

from django.contrib.auth import get_user_model

User = get_user_model()


class TopicViewset(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class MessageViewset(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class DelayedMessagesViewset(viewsets.ModelViewSet):
    serializer_class = DelayedMessagesSerializer
    queryset = DelayedMessages.objects.all()
