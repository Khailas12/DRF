from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


"""
mixin is a class which contains a combination of methods from other classes
"""

# compressed version of the one commented below
class SnippetList(generics.CreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


"""  
class SnippetList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
    ):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def get(self, request, **kwargs):
        return self.list(request, **kwargs)
    
    def post(self, request, **kwargs):
        return self.create(request, **kwargs)
    

class SnippetDetail(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, generics.GenericAPIView
    ):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)
    
    def put(self, request, **kwargs):
        return self.update(request, **kwargs)
    
    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)
"""