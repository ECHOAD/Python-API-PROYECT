from django.contrib.auth import get_user_model, authenticate
from core import models
from django.utils.translation import gettext as _
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = models.Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return models.Tag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
