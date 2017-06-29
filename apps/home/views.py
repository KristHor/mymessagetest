from django.conf import settings
from django.views import generic
from apps.chat.serializer import MessageSerializer
from apps.chat.models import ChatMessage
from rest_framework import generics

from apps.chat import models

from apps.home.utils import getUser

class HomePageView(generic.ListView):
    template_name = 'landing/home.html'
    model = models.ChatMessage
    ordering = 'created'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.session.setdefault(
            'user', getUser()
        )
        context['user'] = user
        context['ws_server_path'] = 'ws://{}:{}/'.format(
            settings.WS_SERVER_HOST,
            settings.WS_SERVER_PORT,
        )
        return context


class MessageList(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = MessageSerializer







