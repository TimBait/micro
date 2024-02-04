from rest_framework.generics import ListAPIView
from . import serializers
from . import models


class UserListAPIView(ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.all()