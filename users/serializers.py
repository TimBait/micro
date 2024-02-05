from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'login', 'password', 'is_active']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance.login = validated_data.get('login', instance.login)
        #instance.password = validated_data.get('password', instance.password)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance