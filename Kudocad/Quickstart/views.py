from django.contrib.auth.models import Group, User
from rest_framework import filters, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from Kudocad.Quickstart.models import Movie

from Kudocad.Quickstart.serializers import GroupSerializer, MovieSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = [
        f.name for f in Movie._meta.fields if f.name not in ['id']]
    ordering_fields = [
        f.name for f in Movie._meta.fields if f.name not in ['id']]
