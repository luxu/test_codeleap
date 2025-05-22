from rest_framework import serializers

from core.models import Careers

class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = (
            'id',
            'title',
            'content',
            'username',
            'created_datetime',
            'author_ip'
        )


class CareersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = (
            'title',
            'content',
            'username',
            'created_datetime',
            'author_ip'
        )


class CareersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = (
            'title',
            'content',
            'author_ip'
        )
