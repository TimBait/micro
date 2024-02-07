from rest_framework import serializers
from users.models import User
import re

class PasswordValidator:
    def __init__(self, regex):
        self.regex = re.compile(regex)

    def __call__(self, value):
        if not self.regex.match(value):
            raise serializers.ValidationError("Пароль не соответствует требуемому формату! Можно использовать только буквы и цифры !")

password_regex_validator = PasswordValidator(
    regex=r'^[a-zA-Z0-9]+$'
)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(validators=[password_regex_validator])
    # token = serializers.CharField(max_length=255, read_only=True)
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



