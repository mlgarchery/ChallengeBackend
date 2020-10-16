# Django
from django.urls import path

# Api
from api import views


urlpatterns = [
    path('api/artists/', views.ListLastArtists.as_view()),
]
