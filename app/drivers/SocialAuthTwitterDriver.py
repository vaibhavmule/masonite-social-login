import tweepy
import os

from masonite.drivers.BaseDriver import BaseDriver


class SocialAuthTwitterDriver(BaseDriver):

    def __init__(self, Request, SocialAuthConfig, Application):
        self.config = SocialAuthConfig
        self.appconfig = Application
        self.request = Request
        self.oauth =  tweepy.OAuthHandler(
            self.config.DRIVERS['twitter']['consumer_key'],
            self.config.DRIVERS['twitter']['consumer_secret'],
        )

    def start_auth(self):
        auth_url = self.oauth.get_authorization_url(True)
        self.request.session.set('request_token', self.oauth.request_token)
        return self.request.redirect(auth_url)   

    def callback(self):
        verifier = self.request.input('oauth_verifier')
        token = self.request.session.get('request_token')
        self.request.session.delete('request_token')
        self.oauth.request_token = token
        try:
            self.oauth.get_access_token(verifier)
        except tweepy.TweepError:
            print('Error, failed to get access token')
        self.request.session.set('access_key_tw', self.oauth.access_token)
        self.request.session.set('access_secret_tw', self.oauth.access_token_secret)
        return self.request.redirect('/')

    def get_api(self):
        if self.request.session.has('access_key_tw'):
            access_key = self.request.session.get('access_key_tw')
            access_secret = self.request.session.get('access_secret_tw')
            self.oauth.set_access_token(access_key, access_secret)
            api = tweepy.API(self.oauth)
            return api
        return None

    def logout(self):
        if self.request.session.has('access_key_tw'):
            # request.session.reset()
            self.request.session.delete('access_key_tw')
        return self.request.redirect('/')
