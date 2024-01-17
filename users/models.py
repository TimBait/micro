from django.conf import settings
from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

