## Masonite Twitter Social Login

![Masonite Twitter Social Login](https://i.imgur.com/lVjnwSN.jpg)
## Installation:

```
    $ pip3 install masonite-cli :: (may need sudo if using UNIX) ::
    $ git clone https://github.com/vaibhavmule/masonite-twitter-social-login.git
    $ cd masonite-twitter-social-login
    $ pipenv install
```

## Prerequsite

You need to set follwing environment key in `.env` file.

```
TWITTER_CONSUMER_KEY=
TWITTER_CONSUMER_SECRET=
TWITTER_REDIRECT=http://localhost:8000/complete/twitter/
```

Now just run the server:

```
$ craft serve
```


Go to `http://localhost:8000/`
****


Happy Crafting!
