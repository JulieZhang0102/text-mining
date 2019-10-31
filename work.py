from twython import Twython
# Replace the following strings with your own keys and secrets
TOKEN = '979065615498571776-vU0VzPsCqwjOPnSvKmMNvk8FO18zBKW'
TOKEN_SECRET = '4xai1LUPL5e9NNkZ52rUj1kccdRsT4t0dnWFgLbcfn2sg'
CONSUMER_KEY = 'kDg4HbFY7qy984eIIa3DEfyyk'
CONSUMER_SECRET = 'GDj7O1hbzoew3PT8RO0rjuggnzzl8PldYJrhzOagZmwqANyJ1h'


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="Halloween", count=50)


for status in data['statuses']:
    print(status['text'])