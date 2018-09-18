''' A Module Description '''
from social_core.actions import do_auth, do_complete, do_disconnect

class SocialAppAuthController:
    ''' Class Docstring Description '''

    def auth(self, Request):
        strategy = Request.param('strategy')
        print(strategy)

    def callback(self, Request):
        pass