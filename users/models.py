from django.conf import settings
from django.db import models


class User(models.Model):
    login = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        ordering = ['id']

