# Tools
import base64
import requests
import os


class SpotifyAuth(object):
    SPOTIFY_URL_AUTH = "https://accounts.spotify.com/authorize/"
    SPOTIFY_URL_TOKEN = "https://accounts.spotify.com/api/token/"
    RESPONSE_TYPE = "code"
    HEADER = "application/x-www-form-urlencoded"
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    CALLBACK_URL = "http://localhost:5000/auth"
    SCOPE = "user-read-email user-read-private"

    def base64_credentials(self):
        return base64.b64encode(
                    f"{self.CLIENT_ID}:{self.CLIENT_SECRET}".encode()
               ).decode()

    def getAuth(self, client_id, redirect_uri, scope):
        return (
            f"{self.SPOTIFY_URL_AUTH}"
            f"?client_id={client_id}"
            f"&redirect_uri={redirect_uri}"
            f"&scope={scope}"
            f"&response_type={self.RESPONSE_TYPE}"
        )

    def getToken(self, code, redirect_uri):
        body = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
        }

        headers = {
            "Content-Type": self.HEADER,
            "Authorization": f"Basic {self.base64_credentials()}",
        }

        post = requests.post(
            self.SPOTIFY_URL_TOKEN,
            params=body,
            headers=headers
        )
        return self.handleToken(post.json())

    def handleToken(self, response, f_dict=None):
        fields_dict = f_dict or ["access_token", "expires_in", "refresh_token"]
        if "error" in response:
            return response
        return {
            key: response[key]
            for key in fields_dict
        }

    def refreshAuth(self, refresh_token):
        body = {"grant_type": "refresh_token", "refresh_token": refresh_token}

        headers = {
            "Content-Type": self.HEADER,
            "Authorization": f"Basic {self.base64_credentials()}",
        }

        post_refresh = requests.post(
            self.SPOTIFY_URL_TOKEN,
            data=body,
            headers=headers
        )

        return self.handleToken(
            post_refresh.json(),
            ["access_token", "expires_in"]
        )

    def getUser(self):
        return self.getAuth(
            self.CLIENT_ID, f"{self.CALLBACK_URL}/callback", self.SCOPE,
        )

    def getUserToken(self, code):
        return self.getToken(
            code,
            f"{self.CALLBACK_URL}/callback"
        )
