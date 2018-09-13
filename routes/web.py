''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show'),

    # Twitter
    Get().route('/auth', 'OauthController@send_to_twitter'),
    Get().route('/complete/twitter', 'OauthController@complete'),
    Get().route('/logout', 'OauthController@logout'),
]
