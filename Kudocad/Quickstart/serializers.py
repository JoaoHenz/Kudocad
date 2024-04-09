from dataclasses import fields
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from Kudocad.Quickstart.models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id')

    class Meta:
        model = Movie
        fields = [f.name for f in model._meta.fields if f.name not in ['public_id']]
