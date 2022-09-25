from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:pk>/', views.PrivateChatRoomView.as_view(), name='room'), 
    path('', views.ChatListView.as_view(), name='chat_list')
]