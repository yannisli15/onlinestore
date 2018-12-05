from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discounted_price',
                    'is_featured', 'is_popular', 'is_published',)
    list_display_links = ('id', 'title')
    list_filter = ('sub_category', 'is_published', 'is_featured', 'is_popular',)
    list_editable = ('is_published',)


admin.site.register(Listing, ListingAdmin)
