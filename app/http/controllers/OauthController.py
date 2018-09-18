''' A Module Description '''


class OauthController:
    ''' Class Docstring Description '''

    def auth(self, SocialAuth):
        return SocialAuth.auth()

    def callback(self, Request, SocialAuth):
        SocialAuth.callback()
        return Request.redirect('/')