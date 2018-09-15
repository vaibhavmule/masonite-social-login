''' A Module Description '''

class WelcomeController:
    ''' Class Docstring Description '''

    def show(self, SocialAuth):
        ''' Show Home Template '''
        api = SocialAuth.get_api()
        if api:
            user = api.me()
        else:
            user = None
        return view('index', {'user': user,})
