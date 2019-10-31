# Import Halloween vocabulary word list

def read_file_to_list(path_to_file):
    """
    reads file of words, return a list of words
    """
    f = open(path_to_file)
    tweet_list = []
    words = []
    for line in f:
        line.strip()
        tweet_list.append(line)
    for i in range(len(tweet_list)):
        tweet_list[i].split()
        for word in tweet_list[i]:
            word.strip()
            words.append(word)
    return words

tweet_word = read_file_to_list("assignment2/text-mining/Halloween_text")
# print(tweet_word)

def count_word_frequency(tweets):
    dictionary = {}
    for letter in tweets:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

# print(count_word_frequency(tweet_word))


# def most_frequent(text):
#     letters = [letter.lower() for letter in text if letter.isalpha()]
#     dictionary = make_dict(letters)
#     result = []
#     for key in dictionary:
#         result.append((dictionary[key], key))
#     result.sort(reverse=True)
#     for count, letter in result:
#         print(letter, count)

# most_frequent(text)

"custom"
"party"
"pumpkin"
"joker"
"horror"