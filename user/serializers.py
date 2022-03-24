from rest_framework import serializers

from user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "api_key", "is_admin")
        read_only_fields = ("api_key", "is_admin")
