from nltk.sentiment.vader import SentimentIntensityAnalyzer

def read_file_to_list(path_to_file):
    """
    reads file of words, return a list of words
    """
    f = open(path_to_file)
    tweet_list = []
    for line in f:
        line = line.replace('\n', '')
        tweet_list.append(line)
    return tweet_list

tweets = read_file_to_list("assignment2/text-mining/Halloween_text")

score_list_neg = []
score_list_neu = []
score_list_pos = []
score_list_compound = []

for i in range(len(tweets)):
    sentence = tweets[i]
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    score_list_neg.append(score['neg'])
    score_list_neu.append(score['neu'])
    score_list_pos.append(score['pos'])
    score_list_compound.append(score['compound'])

avg_neg = sum(score_list_neg)/100
avg_neu = sum(score_list_neu)/100
avg_pos = sum(score_list_pos)/100
avg_compound = sum(score_list_compound)/100

print('The average negative score is {:.2f}; neutral score is {:.2f}; positive score is {:.2f}; compound score is {:.2f}.'.format(avg_neg, avg_neu,avg_pos,avg_compound))