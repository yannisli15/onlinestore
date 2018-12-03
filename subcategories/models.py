import uuid

from django.db import models

from categories.models import Category


class SubCategory(models.Model):
    id = uuid.uuid4().hex if id is None else id
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
