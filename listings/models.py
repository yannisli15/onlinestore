import uuid
from datetime import datetime
from django.db import models

from subcategories.models import SubCategory


class Listing(models.Model):

    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    id = uuid.uuid4().hex if id is None else id
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    keywords = models.TextField(blank=True)
    discounted_price = models.IntegerField(default=0, blank=True)
    description = models.TextField(blank=True)
    brand_Name = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    material_composition = models.CharField(max_length=200, blank=True)
    return_days = models.CharField(max_length=100, blank=True)
    warranty_days = models.CharField(max_length=100, blank=True)

    is_male = models.BooleanField(default=None, blank=True)
    is_female = models.BooleanField(default=None, blank=True)
    is_child = models.BooleanField(default=None, blank=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    photo_main = models.CharField(max_length=200)
    photo_1 = models.CharField(max_length=200, blank=True)
    photo_2 = models.CharField(max_length=200, blank=True)
    photo_3 = models.CharField(max_length=200, blank=True)
    photo_4 = models.CharField(max_length=200, blank=True)
    photo_5 = models.CharField(max_length=200, blank=True)
    photo_6 = models.CharField(max_length=200, blank=True)
    photo_7 = models.CharField(max_length=200, blank=True)
    photo_8 = models.CharField(max_length=200, blank=True)
    photo_9 = models.CharField(max_length=200, blank=True)
    photo_10 = models.CharField(max_length=200, blank=True)
    photo_11 = models.CharField(max_length=200, blank=True)
    photo_12 = models.CharField(max_length=200, blank=True)
    photo_13 = models.CharField(max_length=200, blank=True)
    photo_14 = models.CharField(max_length=200, blank=True)
    photo_15 = models.CharField(max_length=200, blank=True)
    size_1 = models.CharField(max_length=50, blank=True)
    size_2 = models.CharField(max_length=50, blank=True)
    size_3 = models.CharField(max_length=50, blank=True)
    size_4 = models.CharField(max_length=50, blank=True)
    size_5 = models.CharField(max_length=50, blank=True)
    size_6 = models.CharField(max_length=50, blank=True)
    size_7 = models.CharField(max_length=50, blank=True)
    size_8 = models.CharField(max_length=50, blank=True)
    size_9 = models.CharField(max_length=50, blank=True)
    size_0 = models.CharField(max_length=50, blank=True)
    size_11 = models.CharField(max_length=50, blank=True)
    size_12 = models.CharField(max_length=50, blank=True)
    size_13 = models.CharField(max_length=50, blank=True)
    size_14 = models.CharField(max_length=50, blank=True)
    size_15 = models.CharField(max_length=50, blank=True)
    color_1 = models.CharField(max_length=50, blank=True)
    color_photo1 = models.CharField(max_length=50, blank=True)
    color_2 = models.CharField(max_length=50, blank=True)
    color_photo2 = models.CharField(max_length=50, blank=True)
    color_3 = models.CharField(max_length=50, blank=True)
    color_photo3 = models.CharField(max_length=50, blank=True)
    color_4 = models.CharField(max_length=50, blank=True)
    color_photo4 = models.CharField(max_length=50, blank=True)
    color_5 = models.CharField(max_length=50, blank=True)
    color_photo5 = models.CharField(max_length=50, blank=True)

    listed_date = models.DateTimeField(default=datetime.now, blank=True)

    # discounted_percent = ((price - discounted_price) / price) * 100

    def __str__(self):
        return self.title

    def discounted_percent(self):
        return round(float(((self.price - self.discounted_price) / self.price) * 100), 1)
