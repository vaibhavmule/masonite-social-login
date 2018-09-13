''' A Module Description '''

from app.integrations.IntegrationTwitterDriver import IntegrationTwitterDriver

class OauthController:
    ''' Class Docstring Description '''

    def send_to_twitter(self, Request):
        return IntegrationTwitterDriver().start_auth(Request)

    def complete(self, Request):
        return IntegrationTwitterDriver().callback(Request)

    def logout(self, Request):
        return IntegrationTwitterDriver().logout(Request)
