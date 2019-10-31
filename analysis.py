# Import Halloween vocabulary word list

def read_file_to_list(path_to_file):
    """
    reads file of words, return a list of words
    """
    f = open(path_to_file)
    tweet_list = []
    words = []
    words_final = []
    for line in f:
        line.strip()
        line = line.lower()
        tweet_list.append(line)
    for i in range(len(tweet_list)):
        word = tweet_list[i].split()
        words.append(word)
    for i in words:
        words_final += i

        # for word in tweet_list[i]:
        #     word.strip()
        #     words.append(word)
    return words_final

tweet_word = read_file_to_list("assignment2/text-mining/Halloween_text")

def stop_word(tweet):
    stopwords = []
    new_tweet = []
    with open('assignment2/text-mining/stopwords.txt') as f:
        for line in f:
            # line.strip("\r\n")
            line = line.replace(' \n','')
            stopwords.append(line)
    # for word in stopwords:
    #     if word in tweet:
    #         tweet.remove(word)
    for i in range(len(tweet)):
        word = tweet[i]
        if word not in stopwords:
            new_tweet.append(word)
    return new_tweet
    # print(stopwords)
    # print(tweet)
    # return tweet

tweet_word_after_stopwords = stop_word(tweet_word)
# print(tweet_word_after_stopwords)

def count_word_frequency(tweets):
    dictionary = {}
    for letter in tweets:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

word_dictionary = count_word_frequency(tweet_word_after_stopwords)


def most_frequent(dictionary):
    result = []
    for key, value in dictionary.items():
        result.append((value, key))
    result.sort()
    result.reverse()
    return result

word_frequency = most_frequent(word_dictionary)

top_ten_word = print(word_frequency[:10])