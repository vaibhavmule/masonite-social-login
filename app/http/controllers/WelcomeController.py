''' A Module Description '''

from app.integrations.IntegrationTwitterDriver import IntegrationTwitterDriver

class WelcomeController:
    ''' Class Docstring Description '''

    def show(self, Request):
        ''' Show Home Template '''
        api = IntegrationTwitterDriver().get_api(Request)
        if api:
            user = api.me()
        else:
            user = None
        return view('index', {'user': user})
