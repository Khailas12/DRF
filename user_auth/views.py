from rest_framework import generics
from .serializers import UserSerializer
from myapp.models import Snippet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    
    def pre_save(self, obj):    # this overriding handles uniqueness for a users belongings
        obj.owner = self.request.user
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def pre_save(self, obj):
        self.owner = self.request.user