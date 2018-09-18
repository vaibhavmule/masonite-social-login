from requests_oauthlib import OAuth1Session

from masonite.drivers.BaseDriver import BaseDriver


class SocialAuthTwitterDriver(BaseDriver):

    def __init__(self, Request, SocialAuthConfig, Application):
        self.config = SocialAuthConfig
        self.appconfig = Application
        self.request = Request
        self.twitter = OAuth1Session(
            self.config.DRIVERS['twitter']['consumer_key'],
            client_secret=self.config.DRIVERS['twitter']['consumer_secret'],
        )

    def auth(self):
        request_token = self.twitter.fetch_request_token('https://api.twitter.com/oauth/request_token')
        auth_url = self.twitter.authorization_url('https://api.twitter.com/oauth/authenticate')
        self.request.session.set('request_token', request_token)
        return self.request.redirect(auth_url)

    def callback(self):
        verifier = self.request.input('oauth_verifier')
        token = self.request.session.get('request_token')
        self.request.session.delete('request_token')

        self.twitter.resource_owner_key = token['oauth_token']
        self.twitter.resource_owner_secret = token['oauth_token_secret']

        self.twitter.fetch_access_token('https://api.twitter.com/oauth/access_token', verifier=verifier)
        return self.request.redirect('/')