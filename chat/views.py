from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Topic, Message, DelayedMessages
from .forms import RegistrationForm

class TopicView(LoginRequiredMixin, CreateView):
    model = Topic
    login_url = 'chat:login'
    template_name = 'chat/index.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = Topic.objects.order_by('-id')
        return context

    def get_success_url(self):
        success_url = reverse_lazy("chat:topic")
        return success_url

class MessageView(LoginRequiredMixin, ListView):
    login_url = 'chat:login'
    template_name = 'chat/room.html'
    context_object_name = 'messages'
    paginate_by = 5

    def get_queryset(self):
        return Message.objects.filter(topic_message__pk=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic_id'] = self.kwargs['pk']
        return context

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'chat/registration.html'
    success_url = reverse_lazy('chat:login')

class DelayedMessageView(LoginRequiredMixin, CreateView):
    login_url = 'chat:login'
    model = DelayedMessages
    template_name = 'chat/delayedmessage.html'
    fields = ('text', 'date_time', 'anonymous')

    def form_valid(self, form):
        form.instance.topic_message_id = self.kwargs['pk']
        form.instance.sender_name = self.request.user.username
        return super().form_valid(form)
    
    def get_success_url(self):
        success_url = reverse_lazy("chat:room", args=(self.kwargs["pk"],))
        return success_url



