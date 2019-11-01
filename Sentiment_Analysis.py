from nltk.sentiment.vader import SentimentIntensityAnalyzer
import ast

# Import tweets gathered as a list
with open('Halloween_text_list', 'r') as f:
    tweets_list = ast.literal_eval(f.read())

# Create lists for different sentiments
score_list_neg = []
score_list_neu = []
score_list_pos = []
score_list_compound = []

# Sentiment analysis for each tweet in the list, and resulting sentiment scores are added to each sentiment list
for i in range(len(tweets_list)):
    sentence = tweets_list[i]
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    score_list_neg.append(score['neg'])
    score_list_neu.append(score['neu'])
    score_list_pos.append(score['pos'])
    score_list_compound.append(score['compound'])

# Calculate the average score of each sentiment
avg_neg = sum(score_list_neg)/100
avg_neu = sum(score_list_neu)/100
avg_pos = sum(score_list_pos)/100
avg_compound = sum(score_list_compound)/100

# Print out the average score for each sentiment, keep 2 decimal places
print('The average negative score is {:.2f}; neutral score is {:.2f}; positive score is {:.2f}; compound score is {:.2f}.'.format(avg_neg, avg_neu,avg_pos,avg_compound))