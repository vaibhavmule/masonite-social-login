from requests_oauthlib import OAuth1Session

from masonite.drivers.BaseDriver import BaseDriver


class SocialAuthTwitterDriver(BaseDriver):

    request_token_url = 'https://api.twitter.com/oauth/request_token'
    authorization_base_url = 'https://api.twitter.com/oauth/authenticate'
    access_token_url = 'https://api.twitter.com/oauth/access_token'
    request_token = ''

    def __init__(self, Request, SocialAuthConfig):
        self.config = SocialAuthConfig
        self.request = Request
        self.twitter = OAuth1Session(
            self.config.DRIVERS['twitter']['consumer_key'],
            client_secret=self.config.DRIVERS['twitter']['consumer_secret'],
        )

    def auth(self):
        request_token = self.twitter.fetch_request_token(self.request_token_url)
        self.request_token = request_token  
        return self.request.redirect(self.twitter.authorization_url(self.authorization_base_url))

    def callback(self):
        verifier = self.request.input('oauth_verifier')

        self.twitter.resource_owner_key = self.request_token['oauth_token']
        self.twitter.resource_owner_secret = self.request_token['oauth_token_secret']
        
        return self.twitter.fetch_access_token(self.access_token_url, verifier=verifier)