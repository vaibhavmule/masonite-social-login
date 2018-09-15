''' Mail Settings '''

import os



'''
|--------------------------------------------------------------------------
| Social Auth Driver
|--------------------------------------------------------------------------
|
| Supported: 'twitter'
|
'''

DRIVER = os.getenv('SOCIAL_AUTH_DRIVER', 'twitter')

'''
|--------------------------------------------------------------------------
| Social Auth Drivers
|--------------------------------------------------------------------------
|
| Different drivers you can use for social auth.
|
'''

DRIVERS = {
    'twitter': {
        'consumer_key': os.getenv('TWITTER_CONSUMER_KEY', ''),
        'consumer_secret': os.getenv('TWITTER_CONSUMER_SECRET', ''),
        'redirect': os.getenv('TWITTER_REDIRECT', 'http://localhost:8000/complete/twitter/'),
    },
}
