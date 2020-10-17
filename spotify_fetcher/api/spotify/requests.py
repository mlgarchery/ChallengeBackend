# Tool
import requests
from functools import wraps

# Api
from api.models import AccessToken, Artist
from api.spotify.token import manage_content_request_error


def manage_error_response(request_function):
    @wraps(request_function)
    def wrap(*args, **kwargs):
        print("wrapped")
        response_json = request_function(*args, **kwargs)
        print("manage errors")
        if "error" in response_json:
            manage_content_request_error(response_json)
        return response_json
    return wrap


@manage_error_response
def request_artist(href):
    """
    Request the data of one artist
    Add the retrieved_date (timezone.now()) to the data
    then use the serializer to validate and save it.
    """
    access_token = AccessToken.objects.last().access_token
    response = requests.get(
        href,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json()


@manage_error_response
def requests_new_releases():
    access_token = AccessToken.objects.last().access_token
    artist_count = Artist.objects.count()
    response = requests.get(
        "https://api.spotify.com/v1/browse/new-releases"
        f"?offset={artist_count}"
        f"&limit=20",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json()
