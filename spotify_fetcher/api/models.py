# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Artist(models.Model):
    id = models.CharField(primary_key=True, max_length=300)
    external_urls = models.JSONField()
    # {"spotify" : "https://open.spotify.com/artist/0OdUWJ0sBjDrqHygGUXeCF"}
    followers = models.JSONField()
    # { "href" : null, "total" : 306565}
    genres = ArrayField(models.CharField(max_length=300))
    # [ "indie folk", "indie pop" ],
    href = models.URLField()
    images = ArrayField(models.JSONField())
    # [{"height": h, "width": w, "url": u}, {}..]
    name = models.CharField(max_length=300)
    popularity = models.IntegerField()  # 0 < p < 100
    type = models.CharField(max_length=300)  # "artist"
    uri = models.CharField(max_length=300)  # spotify url of the artist

    retrieved_date = models.DateTimeField()


class AccessToken(models.Model):
    access_token = models.CharField(max_length=400)
    refresh_token = models.CharField(max_length=400)
    expires_in = models.IntegerField()
    # time after retrieved date until when the access token is valid
    retrieved_date = models.DateTimeField()
