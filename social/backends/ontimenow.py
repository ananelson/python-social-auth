"""
OnTimeNow OAuth2 backend, docs at:
    http://psa.matiasaguirre.net/docs/backends/ontimenow.html
"""
from social.backends.oauth import BaseOAuth2

class OnTimeNowOAuth2(BaseOAuth2):
    """OnTimeNow OAuth2 authentication backend"""
    name = 'ontimenow'

    AUTHORIZATION_PATH = '/auth'
    ACCESS_TOKEN_PATH = '/api/oauth2/token'
    REFRESH_TOKEN_PATH = None
    REVOKE_TOKEN_PATH = None

    def get_key_and_secret(self):
        return self.setting('client-id'), self.setting('client-secret')

    def authorization_url(self):
        return self.setting('base-url') + self.AUTHORIZATION_PATH

    def access_token_url(self):
        return self.setting('base-url') + self.ACCESS_TOKEN_PATH

    def refresh_token_url(self):
        if self.REFRESH_TOKEN_PATH:
            return self.setting('base-url') + self.REFRESH_TOKEN_PATH

    def revoke_token_base_url(self):
        if self.REVOKE_TOKEN_PATH:
            return self.setting('base-url') + self.REVOKE_TOKEN_PATH

    def get_user_id(self, details, response):
        return details['id']

    def get_user_details(self, response):
        """
        Return user details from OnTimeNow account. Store access_token for subsequent API calls.
        """
        details = response['data']
        details['access_token'] = response['access_token']
        return response['data']
