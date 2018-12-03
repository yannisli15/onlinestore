from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from categories.models import Category
from listings.models import Listing
from subcategories.models import SubCategory


# All listings
def listings(request, subcat_id):
    if subcat_id == 0:
        listings = Listing.objects.order_by('-listed_date').filter(is_published=True)
        key = 'All'
    else:
        listings = Listing.objects.order_by('-listed_date').filter(sub_category_id=subcat_id)
        current_subcat = SubCategory.objects.get(id=subcat_id)
        key = current_subcat.title

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listing = paginator.get_page(page)

    catagories = Category.objects.order_by('title')

    dictionary = {}
    for category in catagories:
        sub_categories = SubCategory.objects.order_by('title').filter(category=category)
        dictionary[category] = {}
        for sub_category in sub_categories:
            dictionary[category][sub_category.id] = sub_category.title
    context = {
        'listings': page_listing,
        'total_listings': listings,
        'dictionary': dictionary,
        'categories': catagories,
        'key': key.title,
    }
    return render(request, 'listings/listings.html', context)


def search(request):
    global listings, keywords
    queryset_list = Listing.objects.order_by('-listed_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords != '':
            listings = queryset_list.filter(keywords__icontains=keywords,
                                            is_published=True)
        else:
            listings = queryset_list.all()

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listing = paginator.get_page(page)

    catagories = Category.objects.order_by('title')
    dictionary = {}
    for category in catagories:
        sub_categories = SubCategory.objects.order_by('title').filter(category=category)
        dictionary[category] = {}
        for sub_category in sub_categories:
            dictionary[category][sub_category.id] = sub_category.title
    context = {
        'listings': page_listing,
        'total_listings': listings,
        'dictionary': dictionary,
        'categories': catagories,
        'key': 'all' if keywords is '' else request.GET['keywords']
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    photos = [
        listing.photo_1, listing.photo_2, listing.photo_3, listing.photo_4,
        listing.photo_5, listing.photo_6, listing.photo_7, listing.photo_8,
        listing.photo_9, listing.photo_10, listing.photo_11, listing.photo_12,
        listing.photo_13, listing.photo_14, listing.photo_15,
    ]

    catagories = Category.objects.order_by('title')
    dictionary = {}
    for category in catagories:
        sub_categories = SubCategory.objects.order_by('title').filter(category=category)
        dictionary[category] = {}
        for sub_category in sub_categories:
            dictionary[category][sub_category.id] = sub_category.title

    context = {
        'listing': listing,
        'dictionary': dictionary,
        'photos': photos,
    }
    return render(request, 'listings/listing.html', context)

# { < Category: Clothings >: {'Clothings': [{'id': 3, 'category_id': 1, 'title': 'Trousers'},
#                                           {'id': 2, 'category_id': 1, 'title': 'Blouses'},
#                                           {'id': 1, 'category_id': 1, 'title': 'Dresses'}]},
#   < Category: Shoes >: {'Shoes': [{'id': 5, 'category_id': 2, 'title': 'Boots'},
#                                   {'id': 4, 'category_id': 2, 'title': 'Slippers'}]}}
