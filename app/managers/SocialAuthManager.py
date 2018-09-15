from masonite.managers import Manager

class SocialAuthManager(Manager):
    config = 'SocialAuthConfig'
    driver_prefix = 'SocialAuth'
