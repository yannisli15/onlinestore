from django import template

from categories.models import Category
from subcategories.models import SubCategory

register = template.Library()


@register.simple_tag
def cat_subcat():
    catagories = Category.objects.order_by('title')

    dictionary = {}
    for category in catagories:
        sub_categories = SubCategory.objects.order_by('title').filter(category=category)
        dictionary[category] = {}
        for sub_category in sub_categories:
            dictionary[category][sub_category.id] = sub_category.title

    return dictionary
