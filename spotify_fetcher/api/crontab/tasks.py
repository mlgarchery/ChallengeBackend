# Tools
# Django
from django.utils import timezone

# Api
from api.spotify.token import token_is_valid, refresh_or_remove_token
from api.spotify.requests import request_artist, requests_new_releases
from api.serializers import ArtistSerializer


def retrieve_artist(artist):
    """
    Add the retrieved_date (timezone.now()) to the data
    then use the serializer to validate and save it.
    """
    artist["retrieved_date"] = timezone.now()
    artist_ser = ArtistSerializer(data=artist)
    if artist_ser.is_valid():
        artist_ser.update_or_create()


# execute this on a regular basis
def retrieve_artists():
    if not token_is_valid():
        refresh_or_remove_token()
        return
    new_releases = requests_new_releases()
    # saving the artists
    number_of_artist = 0
    for items in new_releases['albums']['items']:
        for _artist in items["artists"]:
            number_of_artist += 1
            artist = request_artist(_artist['href'])
            retrieve_artist(artist)
    print(f"The job added/updated {number_of_artist} artists.\n")