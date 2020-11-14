from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Article

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

#using serializser class
class ArticleSerialiser(serializers.Serializer):
    title=serializers.CharField(max_length=100)
    author=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=100)
    date=serializers.CharField(max_length=100)
    
    def create(self,validated_data):
        return Article.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.author=validated_data.get('author',instance.author)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance

#using Modelserializer class
class ArticleModelSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['title','author','email','date']