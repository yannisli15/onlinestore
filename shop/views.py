from django.http import HttpResponse
from django.shortcuts import render

from categories.models import Category
from listings.models import Listing
from subcategories.models import SubCategory


def index(request):

    listings = Listing.objects.order_by('-listed_date').filter(is_popular=True)
    listingsf = Listing.objects.order_by('-listed_date').filter(is_featured=True)
    listingsd = Listing.objects.order_by('-listed_date').exclude(discounted_price=0)

    catagories = Category.objects.order_by('title')
    dictionary = {}
    for category in catagories:
        sub_categories = SubCategory.objects.order_by('title').filter(category=category)
        dictionary[category] = {}
        for sub_category in sub_categories:
            dictionary[category][sub_category.id] = sub_category.title

    context = {
        'listings': listings,
        'listingsf': listingsf,
        'listingsd': listingsd,
        'dictionary': dictionary,
    }
    return render(request, 'shop/index.html', context)


def contact(request):

    catagories = Category.objects.order_by('title')
    dictionary = {}
    for category in catagories:
        sub_categories = SubCategory.objects.order_by('title').filter(category=category)
        dictionary[category] = {}
        for sub_category in sub_categories:
            dictionary[category][sub_category.id] = sub_category.title

    context = {
        'dictionary': dictionary,
    }
    return render(request, 'shop/about.html', context)