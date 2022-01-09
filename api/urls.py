from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import TopicViewset, UserViewset, MessageViewset, DelayedMessagesViewset

router = DefaultRouter()
router.register('topics', TopicViewset, basename='topics')
router.register('users', UserViewset, basename='users')
router.register('messages', MessageViewset, basename='messages')
router.register('delayedmessages', DelayedMessagesViewset, basename='delayedmessages')

urlpatterns = [
    
] + router.urls