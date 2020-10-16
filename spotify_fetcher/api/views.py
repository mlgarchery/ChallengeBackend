# Django REST Framework
from rest_framework import generics

# Api
from api.serializers import ArtistSerializer
from api.models import Artist


class ListLastArtists(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()[::-1][:10]
    # 10 recent artists, sorted by last appearing date
