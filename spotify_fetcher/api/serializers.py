from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(source='spotify_id')
    # type = serializers.CharField(source='object_type')

    class Meta:
        model = Artist
        fields = "__all__"