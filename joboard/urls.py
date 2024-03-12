from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<listing_id>/", views.listing_details, name="listing_details"),
]