''' Web Routes '''
from masonite.routes import Get, Post
from masonite.helpers.routes import get
from social_core.actions import do_auth, do_complete, do_disconnect

ROUTES = [
    Get().route('/', 'WelcomeController@show'),

    # Twitter
    Get().route('/auth', 'OauthController@send_to_twitter'),
    Get().route('/complete/twitter', 'OauthController@complete'),
    Get().route('/logout', 'OauthController@logout'),

    # Generic Routes
    RouteGroup([
        get('/url1', ...).name('create'),
        get('/url2', ...).name('update'),
        get('/url3', ...).name('delete'),
    ], 
    prefix='/auth',
    ),
]
