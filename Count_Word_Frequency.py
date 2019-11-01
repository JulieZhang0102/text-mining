import ast

# Import tweets gathered as a list
with open('Halloween_text_list', 'r') as f:
    tweets_list = ast.literal_eval(f.read())

# Function to get all words in tweets into a list
def list_to_wordlist(content):
    '''
    Take a list as input, and return a new list of words used in it
    '''
    tweet_words = []
    words_final = []
    for i in range(len(content)):
        word = content[i].split()
        tweet_words.append(word)
    for i in tweet_words:
        words_final += i
    return words_final

# Get the words list of tweets
tweets_words = list_to_wordlist(tweets_list)

# Function to remove common words listed in stopwords text file
def stop_word(wordlist):
    '''
    Take a list of words and return a new list that excludes words in stopwords (regardless of capitalization)
    '''
    stopwords = []
    word_without_stopwords = []
    with open('stopwords.txt') as f:
        for line in f:
            line = line.replace(' \n','')
            stopwords.append(line)
    for i in range(len(wordlist)):
        word = wordlist[i].lower()
        if word not in stopwords:
            word_without_stopwords.append(word)
    return word_without_stopwords

# Remove common words in tweets
tweet_word_after_stopwords = stop_word(tweets_words)

# Founction to count word frequency
def count_word_frequency(words):
    '''
    Take a list of words and return a dictionary with word and its frequency
    '''
    dictionary = {}
    for letter in words:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

# Count tweet words frequency
word_dictionary = count_word_frequency(tweet_word_after_stopwords)

# Function to arrange words from the most frequent to least
def most_frequent(dictionary):
    '''
    Take a dictionary as input
    and return values and keys as a list based on sorted values (large to small)
    '''
    result = []
    for key, value in dictionary.items():
        result.append((value, key))
    result.sort()
    result.reverse()
    return result

# Sort tweet dictionary according to frequency
word_frequency = most_frequent(word_dictionary)

# Print 10 most frequent words and its frequency
top_ten_word = print(word_frequency[:10])