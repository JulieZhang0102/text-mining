import random

tweet_list = []

def read_file_to_list(path_to_file):
    """
    reads file of words, return a list of words
    """
    f = open(path_to_file)
    for line in f:
        line.strip()
        tweet_list.append(line)
    return tweet_list
# print(read_file_to_list('Halloween_text'))


def jaccard_similarity(sentence1, sentence2): 
    a = set(sentence1.split()) 
    b = set(sentence2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def avg_jaccard_similarity():
    total = 0
    count = 0
    for i in range(1000):
        read_file_to_list('Halloween_text')
        i1 = random.randint(1,100)
        i2 = random.randint(1,100)
        sentence1 = tweet_list[i1]
        sentence2 = tweet_list[i2]
        total += jaccard_similarity(sentence1, sentence2)
        count += 1
    return total / count


if __name__ == "__main__":
    print("After 1000 simulations, the average similarity between randomly chosen two tweets is ", avg_jaccard_similarity())
