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
        'consumer_key': os.getenv('TWITTER_CONSUMER_KEY', 'PHHtIeDCwK5KPcYFN1bKyRFXp'),
        'consumer_secret': os.getenv('TWITTER_CONSUMER_SECRET', 'tvutpxn3qzYcxAQtAYTrzOKqkZYjxhaw44a7rAc6ZkuBRqE047'),
        'redirect': os.getenv('TWITTER_REDIRECT', 'http://localhost:8000/complete/twitter/'),
    },
}
