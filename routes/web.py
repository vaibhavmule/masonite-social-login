''' Web Routes '''
from masonite.routes import Get, Post
from masonite.helpers.routes import get
from masonite.routes import RouteGroup

ROUTES = [
    Get().route('/', 'WelcomeController@show'),

    # Generic Routes
    RouteGroup([
        get('/@strategy:string', 'SocialAppAuthController@auth'),
        get('/@strategy:string/callback', 'SocialAppAuthController@callback'),
    ], 
    prefix='/auth',
    ),
]
