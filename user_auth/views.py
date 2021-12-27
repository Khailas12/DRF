from django.contrib.auth.models import User
from rest_framework import generics

from DRF.myapp.models import Snippet
from .serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
    def pre_save(self, obj):    # this overriding handles uniqueness for a users belongings
        obj.owner = self.request.user
    
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
    def pre_save(self, obj):
        obj.owner = self.request.user