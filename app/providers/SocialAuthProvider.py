from masonite.provider import ServiceProvider

from app.drivers.SocialAuthTwitterDriver import SocialAuthTwitterDriver
from app.managers.SocialAuthManager import SocialAuthManager
from config import social_auth

class SocialAuthProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('SocialAuthConfig', social_auth)
        self.app.bind('SocialAuthTwitterDriver', SocialAuthTwitterDriver)
        self.app.bind('SocialAuthManager', SocialAuthManager(self.app))

    def boot(self, SocialAuthManager, SocialAuthConfig):
        self.app.bind('SocialAuth', SocialAuthManager.driver(SocialAuthConfig.DRIVER))
