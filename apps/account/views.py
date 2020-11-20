from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from account.serializers import UserCreateSerializer
from .models import User


class UserCreateViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserCreateSerializer


