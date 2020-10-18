# Tools
from datetime import timedelta

# Django
from django.test import TestCase
from django.utils import timezone

# Api
from api.models import AccessToken
from api.spotify.token import token_exists, token_is_valid, remove_token
from api.spotify.requests import request_artist, requests_new_releases


class Token(TestCase):

    def setUp(self):
        self.accessToken = AccessToken.objects.create(
            access_token="access",
            refresh_token="refresh",
            expires_in=3600,
            retrieved_date=timezone.now()
        )
        self.accessToken.save()

    def tearDown(self):
        remove_token()

    def test_token_exists(self):
        self.assertEqual(token_exists(), True)
        # deleting the token
        remove_token()
        #
        self.assertEqual(token_exists(), False)

    def test_token_is_valid(self):
        self.assertEqual(token_is_valid(), True)
        # faking an old access token:
        self.accessToken.retrieved_date -= timedelta(
            seconds=self.accessToken.expires_in + 1
        )
        self.accessToken.save()
        #
        self.assertEqual(token_is_valid(), False)


class BadSpotifyRequest(TestCase):

    def setUp(self):
        self.accessToken = AccessToken.objects.create(
            access_token="access",
            refresh_token="refresh",
            expires_in=3600,
            retrieved_date=timezone.now()
        )

    def tearDown(self):
        self.accessToken.delete()

    def test_request_invalid_access_token(self):
        response = request_artist("https://api.spotify.com/v1/artists/0Y5tJX1MQlPlqiwlOH1tJY")
        # travis scott valid href
        self.assertEqual(response["error"]["message"], "Invalid access token")
