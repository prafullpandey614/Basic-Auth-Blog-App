from rest_framework.serializers import ModelSerializer
from .models import Blog
class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)
        
    