# Tool
import requests
from functools import wraps

# Api
from api.models import Artist
from api.spotify.token import get_token, manage_content_request_error


def manage_error_response(request_function):
    @wraps(request_function)
    def wrap(*args, **kwargs):
        response_json = request_function(*args, **kwargs)
        if "error" in response_json:
            manage_content_request_error(response_json)
        return response_json
    return wrap


@manage_error_response
def request_artist(href):
    """
    Request the data of one artist.
    """
    access_token = get_token().access_token
    response = requests.get(
        href,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json()


@manage_error_response
def requests_new_releases():
    """
    Request the next 20 album items from new_release.
    """
    access_token = get_token().access_token
    artist_count = Artist.objects.count()
    response = requests.get(
        "https://api.spotify.com/v1/browse/new-releases"
        f"?offset={artist_count}"
        f"&limit=40",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json()
