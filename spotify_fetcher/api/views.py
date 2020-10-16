# Django
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.views import View
from django.utils import timezone

# Django REST Framework
from rest_framework.generics import ListAPIView

# Api
from api.serializers import ArtistSerializer
from api.serializers import AccessTokenSerializer
from api.models import Artist
from api.spotify.auth import SpotifyAuth
from api.spotify.utils import token_exists, is_token_valid, refresh_token


class AuthCallback(View):
    """
    If the code params exist, requests the access token, saves it
    and retrieves artists from new release. Then redirects to /api/artists/.

    Otherwise displays an error.
    """

    def get(self, request):
        code = request.GET.get('code', None)
        access_token_response = SpotifyAuth().getUserToken(code)
        access_token_response["retrieved_date"] = timezone.now()
        ser = AccessTokenSerializer(data=access_token_response)
        if ser.is_valid():
            ser.save()
            # retrieve_artists()  # the crontab execute this regularly
            return HttpResponseRedirect("/api/artists/")
        return HttpResponse("<p>Authentication error</p>")


class ListLastArtists(ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all().reverse()
    # sorted by last appearing date

    def get(self, request, *args, **kwargs):
        """
        Checks if an access token already exists.
        Otherwise redirect the user to the Spotify authorize endpoint,
        in order to create one.

        Else, displays the last artists saved localy.
        """
        if not token_exists():
            return HttpResponseRedirect(SpotifyAuth().getUser())

        if not is_token_valid():
            refresh_token()
        return super(ListLastArtists, self).get(request, *args, **kwargs)
