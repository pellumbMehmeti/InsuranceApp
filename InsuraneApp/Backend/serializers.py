from rest_framework import serializers
from .models import User


# PER API te Policies
# class UserListSerializer(serializers.ModelSerializer):
#     owner = serializers.CharField(max_length = 150, allow_blank = True, required = False)
#     name = serializers.CharField(max_length = 50, allow_blank = True, required = False)
#     age = serializers.IntegerField(required = False)
#     photo = serializers.URLField(required = False)
# class Meta:
#     model = User
#     fields = ('id', 'name', 'surname', 'birthday', 'photo')

class UserSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length = 50, blank = False)
    surname = serializers.CharField(max_length = 50, blank = False)
    email = serializers.CharField(max_length= 20,blank = False)
    username = serializers.CharField(max_length = 15, blank = False)
    birthday = serializers.DateTimeField()
    photo = serializers.URLField(blank=False)  #te verifikohet edhe njihere
    address = serializers.CharField(max_length = 50, blank = False)
    password = serializers.CharField(max_length = 15, blank = False)
    created_at = serializers.DateTimeField(auto_now_add=True)

class Meta:
    model = User
    fields = ('id', 'name', 'surname', 'email', 'username', 'password', 'birthday', 'photo', 'address', 'created_at')