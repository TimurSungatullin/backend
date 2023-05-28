from django.contrib.auth import get_user_model
from rest_framework import serializers

from entity.models import Project

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]


class ProjectSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'author',
            'description',
            'price',
        ]
