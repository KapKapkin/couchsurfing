from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import Http404

from .models import PrivateChatRoom, PrivateChatRoomMessageManager
from couchsurfing.mixins import is_ajax


class PrivateChatRoomView(DetailView):
    model = PrivateChatRoom
    context_object_name = 'chat_room'
    template_name = 'chat/chat.html'

    def get_object(self, queryset=None):
        room = super(PrivateChatRoomView, self).get_object(queryset)
        if not self.request.user in room.users.all():
            raise Http404()
        return room

    def get_context_data(self, **kwargs):
        context = super(PrivateChatRoomView, self).get_context_data(**kwargs)
        context['messages'] = self.get_messages()
        return context
        
    def get_messages(self):
        manager = PrivateChatRoomMessageManager()
        return manager.by_room(room=self.get_object())


class ChatListView(ListView):
    model = PrivateChatRoom
    context_object_name = 'chat_list'
    template_name = 'chat/chat_list.html'

    def get_queryset(self):
        query = self.model.objects.filter(users__id__exact=self.request.user.id)
        return query

