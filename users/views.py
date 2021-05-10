from rest_framework import generics

from users.models import User
from users.serializers import UserUpdateSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'username'
