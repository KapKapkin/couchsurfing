from django.db import models 
from django.conf import settings 
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class PrivateChatRoom(models.Model):
    
    id = models.UUIDField(_('id'), 
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        unique=True,)
    
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text="Users who are in this chat")
    
    def __str__(self):
        return self.title 

    def connect_user(self, user):
        '''
        return True if user is connected to users list
        '''
        is_user_added = False 
        if not user in self.users.all():
            self.user.add(user)
            self.save()
            is_user_added = True
        else:
            is_user_added = True
        return is_user_added

    def disconnect_user(self, user):
        '''
        return True if user is remove from user list
        '''
        is_user_removed = False
        if user in self.users.all():
            self.user.remove(user)
            self.save()
            is_user_removed = True
        return is_user_removed

    @property
    def group_name(self):
        '''
        Returns the channels group name that sockets should subsribe to get sent messages 
        as they are generated.
        '''
        return f'PrivateChatRoom-{self.id}'

class PrivateChatRoomMessageManager(models.Model):
    def by_room(self, room ):
        qs = PrivateRoomChatMessage.objects.filter(room=room).order_by('-timestamp')
        return qs


class PrivateRoomChatMessage(models.Model):
    '''
    Chat message created by a user inside a PrivateChatRoom (Foreign Key)
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(PrivateChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False)

    objects = PrivateChatRoomMessageManager()
    
    def __str__(self):
        return self.content if self.content else ''

