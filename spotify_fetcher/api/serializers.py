# Django REST Framework
from rest_framework import serializers

# Api
from api.models import Artist, AccessToken


class ArtistSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(source='spotify_id')
    # type = serializers.CharField(source='object_type')

    class Meta:
        model = Artist
        fields = "__all__"


class AccessTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessToken
        fields = "__all__"
