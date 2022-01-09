from re import template
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import TopicView, MessageView, RegistrationView, DelayedMessageView

app_name = 'chat'
urlpatterns = [
    path('', TopicView.as_view(), name='topic'),
    path('<int:pk>/', MessageView.as_view(), name='room'),
    path('<int:pk>/delayedmeesage', DelayedMessageView.as_view(), name='delayedmessage'),
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
