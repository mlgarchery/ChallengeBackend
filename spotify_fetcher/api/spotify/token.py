# Tools
from datetime import timedelta
from django.utils import timezone

# Api
from api.models import AccessToken
from api.spotify.auth import SpotifyAuth


def token_exists():
    accessToken = AccessToken.objects.last()
    if accessToken:
        return True
    return False


def token_is_valid():
    """
    Returns the validity of the token
    """
    accessToken = AccessToken.objects.last()
    time_limit = accessToken.retrieved_date + \
        timedelta(seconds=accessToken.expires_in)
    if timezone.now() > time_limit:
        return False
    return True


def refresh_token():
    accessToken = AccessToken.objects.last()
    response = SpotifyAuth().refreshAuth(accessToken.refresh_token)
    if "error" not in response:
        accessToken.access_token = response["access_token"]
        accessToken.expires_in = response["expires_in"]
        accessToken.retrieved_date = timezone.now()
        accessToken.save()
