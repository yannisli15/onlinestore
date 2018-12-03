import uuid
from datetime import datetime
from django.db import models


class Contact(models.Model):
    id = uuid.uuid4().hex if id is None else id
    user_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    contacted_date = models.DateTimeField(default=datetime, blank=True)
