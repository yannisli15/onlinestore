from django.contrib import admin

from .models import SubCategory


class SubCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_filter = ('category',)


admin.site.register(SubCategory, SubCatAdmin)
