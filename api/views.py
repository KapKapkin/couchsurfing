from rest_framework.response import Response
from rest_framework.decorators import api_view
from chat.models import PrivateChatRoom
from .serializers import PrivateChatRoomSerializer

@api_view(['GET'])
def getData(request):
    chats = PrivateChatRoom.objects.all()
    serializer = PrivateChatRoomSerializer(chats, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addChat(request):
    serializer = PrivateChatRoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)