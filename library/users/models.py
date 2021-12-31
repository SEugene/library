from uuid import uuid4

from django.db import models


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=64, unique=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
