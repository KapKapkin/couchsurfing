from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import PrivateChatRoom

def index(request):
    return render(request, 'chat/index.html')

def chat_room(request, room_name):
    return render(request, 'chat/chat.html', context={
        'room_name': room_name
    })
