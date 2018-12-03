from django.urls import path
from . import views

urlpatterns = [
    path('<int:subcat_id>/', views.listings, name='listings'),
    path('listing/<int:listing_id>/', views.listing, name='listing'),
    path('search/', views.search, name='search'),
]
