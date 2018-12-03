import uuid

from django.db import models


class Category(models.Model):
    id = uuid.uuid4().hex if id is None else id
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
