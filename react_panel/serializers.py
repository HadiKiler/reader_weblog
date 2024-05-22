from django.contrib.auth.hashers import make_password
from rest_framework.serializers import *
from .models import *
from config import settings



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
        'id',
        'parent',
        'name',
        'image'
        ]

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = [
        'id',
        'name',
        ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
        'id',
        'username',
        'password',
        'image',
        'bio',
        'email',
        'is_staff'
        ]
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        extra_kwargs = {'message':"mmd"}
        fields = [
        'id',
        'user',
        'category',
        'title',
        'content',
        'tags',
        'created_at',
        'published'
        ]
    

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'parent',
            'post',
            'name',
            'email',
            'content',
            'created_at',
        ]


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'post',
            'user'
        ]



