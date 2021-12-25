from django.db.models import fields
from myapp.models import Snippet
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)
    
    class Meta:
        model = Snippet
        fields = [
            'id',
            'username',
            'snippets',
        ]
        
# 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.