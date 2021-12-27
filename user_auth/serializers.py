from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)
    owner = serializers.Field(source='owner.username')  # Field is read only in serialized. updating models sticks with deserialized
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'snippets',
            'owner',
        ]
        
# 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.