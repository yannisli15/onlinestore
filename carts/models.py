import uuid

from django.db import models


class Cart(models.Model):
    id = uuid.uuid4().hex if id is None else id
    listing_id = models.IntegerField()
    user_id = models.IntegerField()
