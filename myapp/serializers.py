from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100
        )
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
    
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