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
    
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        self.instance.title = validated_data.get('title', self.instance.title)
        self.instance.code = validated_data.get('code', self.instance.code)
  
        self.instance.lineous = validated_data.get('lineous', self.instance.lineous)
        self.instance.language = validated_data.get('langauge', self.instance.language)
        self.instance.style = validated_data.get('style', self.instance.style)
        
        instance.save()
        return self.instance