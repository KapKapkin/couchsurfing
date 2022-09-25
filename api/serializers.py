from rest_framework import serializers
from chat.models import PrivateChatRoom

class PrivateChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateChatRoom
        fields = '__all__'
