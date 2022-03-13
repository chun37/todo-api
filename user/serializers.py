from rest_framework import serializers

from user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "api_key", "is_superuser")
        read_only_fields = ("id", "api_key", "is_superuser")
