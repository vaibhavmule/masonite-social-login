from requests_oauthlib import OAuth1Session

from masonite.drivers.BaseDriver import BaseDriver


class SocialAuthTwitterDriver(BaseDriver):

    def __init__(self, Request, SocialAuthConfig):
        self.config = SocialAuthConfig
        self.request = Request
        self.oauth = OAuth1Session(
            self.config.DRIVERS['twitter']['consumer_key'],
            client_secret=self.config.DRIVERS['twitter']['consumer_secret'],
        )

    def auth(self):
        request_token = self.oauth.fetch_request_token('https://api.twitter.com/oauth/request_token')
        auth_url = self.oauth.authorization_url('https://api.twitter.com/oauth/authenticate')
        self.request.session.set('request_token', request_token)
        return self.request.redirect(auth_url)

    def callback(self):
        verifier = self.request.input('oauth_verifier')
        token = self.request.session.get('request_token')
        self.request.session.delete('request_token')

        self.oauth.resource_owner_key = token['oauth_token']
        self.oauth.resource_owner_secret = token['oauth_token_secret']

        self.oauth.fetch_access_token('https://api.twitter.com/oauth/access_token', verifier=verifier)
        return self.request.redirect('/')