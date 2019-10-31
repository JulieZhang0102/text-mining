from twython import Twython
# import tweepy
# import textblob
# from textblob import TextBlob
import re
# from nltk.corpus import stopwords

# Replace the following strings with your own keys and secrets
TOKEN = '979065615498571776-vU0VzPsCqwjOPnSvKmMNvk8FO18zBKW'
TOKEN_SECRET = '4xai1LUPL5e9NNkZ52rUj1kccdRsT4t0dnWFgLbcfn2sg'
CONSUMER_KEY = 'kDg4HbFY7qy984eIIa3DEfyyk'
CONSUMER_SECRET = 'GDj7O1hbzoew3PT8RO0rjuggnzzl8PldYJrhzOagZmwqANyJ1h'


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

# Gather 100 twitter tweets related to "Halloween" since October this year
data = t.search(q="Halloween", lang = 'en', since = "2019-10-01", count=100)

Halloween_text = []
for status in data['statuses']:
    Halloween_text.append(status['text'])
    # print(Halloween_text)
    # print(len(Halloween_text))

# Clean tweets data
def clean_tweet(tweet):
    '''
    '''
    return " ".join(re.sub('([^0-9A-Za-z ]+)|(\w+:\/\/\S+)', "", tweet).split())


# #Clean the URL 
# def clean_tweet(tweet):
#     """
#     removes url and special special chracters
#     """
#     return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split()) #replace the URL with nothing 
#save the cleaned tweets with for loop and create new list and append that 
cleaned_tweets = []
for tweet in Halloween_text:
    tweet = clean_tweet(tweet)
    cleaned_tweets.append(tweet)
print(cleaned_tweets)
# cleaned_tweets = []
# for tweet in Halloween_text:
#     tweet = clean_tweet(tweet)
#     cleaned_tweets.append(tweet)
# print(cleaned_tweets)

#Save the tweets in a text file
f = open('assignment2/text-mining/Halloween_text','w')
content = [cleaned_tweets]
for tweet in content:
    f.write("\n".join(map(lambda x: str(x), tweet)))
    f.close()