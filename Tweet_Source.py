from twython import Twython
import re

# Connect to Twitter using Twython
TOKEN = '979065615498571776-vU0VzPsCqwjOPnSvKmMNvk8FO18zBKW'
TOKEN_SECRET = '4xai1LUPL5e9NNkZ52rUj1kccdRsT4t0dnWFgLbcfn2sg'
CONSUMER_KEY = 'kDg4HbFY7qy984eIIa3DEfyyk'
CONSUMER_SECRET = 'GDj7O1hbzoew3PT8RO0rjuggnzzl8PldYJrhzOagZmwqANyJ1h'

t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

# Search 100 most recent/popular tweets related to "Halloween" in English, excluding retweets and replies.
# Tweet date range is set before 2019/10/30 with the default 7-days limit from the current date
data = t.search(q="Halloween -filter:retweets AND -filter:replies", lang = 'en', result_type='mixed', until = '2019-10-30', count = 100)

# Compile search results in a list
Halloween_text = []
for status in data['statuses']:
    Halloween_text.append(status['text'])

# Function to clean tweets data
def clean_tweet(tweet):
    '''
    clean input tweet to remove special characters and url, but keep spaces
    '''
    return " ".join(re.sub('([^0-9A-Za-z \']+)|(\w+:\/\/\S+)', "", tweet).split())

# Clean tweet results and save cleaned tweets in a new list 
cleaned_tweets = []
for tweet in Halloween_text:
    tweet = clean_tweet(tweet)
    cleaned_tweets.append(tweet)

# Save final cleaned tweet list in a text file, used to analyze
f = open('Halloween_text_list','w')
content = [cleaned_tweets]
f.write("\n".join(map(lambda x: str(x), content)))
f.close()

# Save final cleaned tweets in a text file, easy to visualize
f = open('Halloween_text','w')
content = [cleaned_tweets]
for tweet in content:
    f.write("\n".join(map(lambda x: str(x), tweet)))
    f.close()