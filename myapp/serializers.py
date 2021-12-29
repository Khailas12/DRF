from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippet
        read_only=('owner.username',)
        # owner = serializers.Field(read_only=True)  # Field is read only in serialized. updating models sticks with deserialized
        
        fields = [
            'id',
            'title',
            'code',
            'lineous',
            'language',
            'read_only',
            'style',
        ]
    
    
    # create and update defines how funny fledged instances are created or modfied.
    
    def create(self, validated_data):   # creates and return a new snippet instance
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):     
        # update and return an existing snipptet instance
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
    
        instance.lineous = validated_data.get('lineous', instance.lineous)
        instance.language = validated_data.get('langauge', instance.language)
        instance.style = validated_data.get('style', instance.style)
    
        instance.save()
        return instance