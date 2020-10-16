# Django
from django.urls import path

# Api
from api import views


urlpatterns = [
    path('auth/callback/', views.AuthCallback.as_view()),
    path('api/artists/', views.ListLastArtists.as_view()),
]
