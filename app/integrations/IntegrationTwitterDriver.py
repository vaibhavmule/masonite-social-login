import tweepy
import os

class IntegrationTwitterDriver:

    def __init__(self):
        self.oauth =  tweepy.OAuthHandler(
            os.getenv('TWITTER_CONSUMER_KEY'),
            os.getenv('TWITTER_CONSUMER_SECRET')
        )

    def start_auth(self, request):
        auth_url = self.oauth.get_authorization_url(True)
        request.session.set('request_token', self.oauth.request_token)
        return request.redirect(auth_url)   

    def callback(self, request):
        verifier = request.input('oauth_verifier')
        token = request.session.get('request_token')
        request.session.delete('request_token')
        self.oauth.request_token = token
        try:
            self.oauth.get_access_token(verifier)
        except tweepy.TweepError:
            print('Error, failed to get access token')
        request.session.set('access_key_tw', self.oauth.access_token)
        request.session.set('access_secret_tw', self.oauth.access_token_secret)
        return request.redirect('/')

    def get_api(self, request):
        if request.session.has('access_key_tw'):
            access_key = request.session.get('access_key_tw')
            access_secret = request.session.get('access_secret_tw')
            self.oauth.set_access_token(access_key, access_secret)
            api = tweepy.API(self.oauth)
            return api
        return None

    def logout(self, request):
        if request.session.has('access_key_tw'):
            request.session.delete('access_key_tw')
        return request.redirect('/')
