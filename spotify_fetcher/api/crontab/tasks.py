# Tools
import requests

# Api
from api.models import AccessToken
from api.spotify.token import token_exists, token_is_valid,\
                                            refresh_token


# crontab should exec this more often than retrieve_artists
def check_token():
    if not token_exists():
        return
    if not token_is_valid():
        refresh_token()


def retrieve_artist(href, access_token):
    """
    Retrieve one artist
    Add the retrieved_date (timezone.now()) to the data
    then use the serializer to validate and save it.
    """
    response = requests.get(
        href,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json()


def retrieve_artists():
    access_token = AccessToken.objects.last().access_token
    response = requests.get(
        "https://api.spotify.com/v1/browse/new-releases",
        headers={"Authorization": f"Bearer {access_token}"}
    ).json()
    # saving the artists
    for items in response['albums']['items']:
        for artist in items["artists"]:
            pass
