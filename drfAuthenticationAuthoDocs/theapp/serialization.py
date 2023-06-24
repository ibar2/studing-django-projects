from rest_framework import serializers
from .models import snipet
from django.contrib.auth.models import User


class usersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = snipet
        fields = ['id', 'title', 'code',
                  'language', 'style', 'owner']


class userSerial(serializers.ModelSerializer):
    snipet = serializers.PrimaryKeyRelatedField(
        many=True, queryset=snipet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', "snipet"]
