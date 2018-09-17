''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show'),

    # Twitter
    Get().route('/auth/twitter', 'OauthController@auth'),
    Get().route('/auth/twitter/callback', 'OauthController@callback'),
]
