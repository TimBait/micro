from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator, RegexValidator


class User(models.Model):
    login = models.CharField(db_index=True, unique=True, validators=[MinLengthValidator(4), MaxLengthValidator(40)],
                             verbose_name='Логин')
    password = models.CharField(validators=[MinLengthValidator(8), MaxLengthValidator(40),
                                            RegexValidator(regex=r'^[a-zA-Z0-9]+$')], verbose_name='Пароль')
    email = models.EmailField(max_length=40, validators=[EmailValidator], default=None,
                              verbose_name='Электронная почта')
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'login'

    class Meta:
        db_table = 'users'
        ordering = ['id']