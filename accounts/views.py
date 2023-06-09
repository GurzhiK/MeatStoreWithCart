from .models import UserAccount
from .serializers import UserListSerializer
from rest_framework import generics


class UserList(generics.ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserListSerializer
