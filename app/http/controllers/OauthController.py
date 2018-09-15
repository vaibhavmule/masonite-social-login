''' A Module Description '''


class OauthController:
    ''' Class Docstring Description '''

    def send_to_twitter(self, SocialAuth):
        return SocialAuth.start_auth()

    def complete(self, SocialAuth):
        return SocialAuth.callback()

    def logout(self, SocialAuth):
        return SocialAuth.logout()
