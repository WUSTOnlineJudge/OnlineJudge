from rest_framework import serializers
from .models import User, UserProfile
from django.contrib.auth.hashers import make_password


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, label="用户名")
    password = serializers.CharField(max_length=32, label="密码")
    email = serializers.EmailField(max_length=30, label="邮箱")

    nickname = serializers.CharField(default="", max_length=16, label="昵称", required=False)
    real_name = serializers.CharField(default="", max_length=16, label="真实姓名", required=False)
    blog = serializers.URLField(default="", label="博客", required=False)
    github = serializers.URLField(default="", max_length=16, label="github", required=False)
    sign = serializers.CharField(default="", max_length=16, label="个性签名", required=False)
    school = serializers.CharField(default="", max_length=100, label="学校", required=False)

    def validate_username(self, username):
        if len(User.objects.filter(username=username)) != 0:
            raise serializers.ValidationError("用户已存在")
        return username

    def validate(self, attrs):
        return attrs

    def save(self):
        validated_data = self.validated_data
        print(validated_data)
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            email=validated_data['email']
        )

        UserProfile.objects.create(
            user=user,
            nickname=validated_data['nickname'],
            real_name=validated_data['real_name'],
            blog=validated_data['blog'],
            github=validated_data['github'],
            sign=validated_data['sign'],
            school=validated_data['school']
        )
