# Tool
import requests

# Api
from api.models import AccessToken


def request_artist(href, access_token):
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


def requests_new_releases():
    access_token = AccessToken.objects.last().access_token
    response = requests.get(
        "https://api.spotify.com/v1/browse/new-releases",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json()
