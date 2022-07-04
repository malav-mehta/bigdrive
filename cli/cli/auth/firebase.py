import requests

from ..utils import error

PUBLIC_API_KEY = "AIzaSyAjCD27S-RhZTm6a37AlnM-CAkDmfyS35E"


class FirebaseAuth:
    base_url = "https://identitytoolkit.googleapis.com/v1/{}?key={}"
    refresh_token_slug = "token"
    sign_up_slug = "accounts:signUp"
    sign_in_slug = "accounts:signInWithPassword"

    def __init__(self, api_key):
        self.api_key = api_key

    def sign_up_with_email_and_password(self, email, password):
        result = requests.post(
            self.base_url.format(self.sign_up_slug, self.api_key),
            json={
                "email": email,
                "password": password,
                "returnSecureToken": True
            }
        )
        return result.json()

    def sign_in_with_email_and_password(self, email, password):
        result = requests.post(
            self.base_url.format(self.sign_in_slug, self.api_key),
            json={
                "email": email,
                "password": password,
                "returnSecureToken": True
            }
        )
        return result.json()

    def get_id_token(self, email, password):
        result = self.sign_in_with_email_and_password(email, password)
        error.exit_if_error(result)

        return result["idToken"]


auth = FirebaseAuth(PUBLIC_API_KEY)
