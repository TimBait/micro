from django.conf import settings
from django.db import models
import jwt
from datetime import datetime, timedelta

class User(models.Model):
    login = models.CharField(db_index=True, max_length=40, unique=True)
    password = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'login'

    class Meta:
        db_table = 'users'
        ordering = ['id']


    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False


    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.login

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.login

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.timestamp())  # HERE
        }, settings.SECRET_KEY, algorithm='HS256')

        return token

