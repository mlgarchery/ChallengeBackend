# Tools
import requests
from datetime import timedelta

# Django
from django.utils import timezone

# Api
from api.models import AccessToken
from api.spotify_auth import SpotifyAuth


def token_exists():
    accessToken = AccessToken.objects.last()
    if accessToken:
        return True
    return False


def is_token_valid():
    """
    Returns the validity of the token
    """
    accessToken = AccessToken.objects.last()
    time_limit = accessToken.retrieved_date + \
        timedelta(seconds=accessToken.expires_in)
    if timezone.now() > time_limit:
        return False
    return True


# crontab should exec this more often than retrieve_artists
def check_token():
    if not token_exists():
        return
    if not is_token_valid():
        refresh_token()


def refresh_token():
    accessToken = AccessToken.objects.last()
    response = SpotifyAuth().refreshAuth(accessToken.refresh_token)
    if "error" not in response:
        accessToken.access_token = response["access_token"]
        accessToken.expires_in = response["expires_in"]
        accessToken.retrieved_date = timezone.now()
        accessToken.save()


def retrieve_artists():
    access_token = AccessToken.objects.last().access_token
    response = requests.get(
        "https://api.spotify.com/v1/browse/new-releases",
        headers={"Authorization": f"Bearer {access_token}"}
    ).json()
    # saving the artists
    pass
