from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.serializers import SnippetSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = SnippetSerializer
        
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'snippets',
        ]

    # 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.