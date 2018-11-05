from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .renderers import UserJSONRenderer
from .serializers import UserSerializer, UserListSerializer
class UserListApiView(ListAPIView):
    model = User
    queryset = User.objects.all()
    permissions_classes = (AllowAny, )
    renderer_classes = (UserJSONRenderer, )
    serializer_class = UserListSerializer

#     edhe nihere te verifikohet userserializer ne rast errori

class UserRetrieveApiView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (UserJSONRenderer, )
    serializer_class = UserSerializer

    def retrieve(self, request, user, *args, **kwargs):
        user = User.objects.get(id = user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status = status.HTTP_200_OK)
