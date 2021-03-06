# Tools
from datetime import timedelta
from django.utils import timezone

# Api
from api.models import AccessToken
from api.spotify.auth import SpotifyAuth


def get_token():
    if not AccessToken.objects.all():
        return None
    return AccessToken.objects.last()


def remove_token():
    accessToken = get_token()
    if accessToken:
        accessToken.delete()


def token_exists():
    accessToken = get_token()
    if accessToken:
        return True
    return False


def token_is_valid():
    """
    Returns the validity of the token
    """
    accessToken = get_token()
    time_limit = accessToken.retrieved_date + \
        timedelta(seconds=accessToken.expires_in)
    if timezone.now() > time_limit:
        return False
    return True


def refresh_or_remove_token():
    """
    Refresh the accessToken. If we get 'Refresh token revoked'
    we remove the accessToken.
    """
    accessToken = get_token()
    response = SpotifyAuth().refreshAuth(accessToken.refresh_token)
    if "error" not in response:
        accessToken.access_token = response["access_token"]
        accessToken.expires_in = response["expires_in"]
        accessToken.retrieved_date = timezone.now()
        accessToken.save()
    # {'error': 'invalid_grant', 'error_description': 'Refresh token revoked'}
    else:
        if "invalid_grant" == response["error"]:
            remove_token()
