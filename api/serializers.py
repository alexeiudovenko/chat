from rest_framework import serializers

from chat.models import Topic, Message, DelayedMessages

from django.contrib.auth import get_user_model

User = get_user_model()

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    topic_message = TopicSerializer()

    class Meta:
        model = Message
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')   

class DelayedMessagesSerializer(serializers.ModelSerializer):
    topic_message = TopicSerializer()
    
    class Meta:
        model = DelayedMessages
        fields = '__all__'