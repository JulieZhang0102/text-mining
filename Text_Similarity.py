import random
import ast

# Import tweets gathered as a list
with open('assignment2/text-mining/Halloween_text_list', 'r') as f:
    tweets_list = ast.literal_eval(f.read())

# Function to calculate the similarity between two sentences
def jaccard_similarity(sentence1, sentence2): 
    '''
    Take two sentences/strings as inputs and return similarity between two inputs
    '''
    a = set(sentence1.split()) 
    b = set(sentence2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

# Random select 2 tweets from tweets list and calculate the similarity, repeat for 1000 times and calculate the average similarity
total = 0
for i in range(1000):
    i1 = random.randint(0,len(tweets_list)-1)
    i2 = random.randint(0,len(tweets_list)-1)
    sentence1 = tweets_list[i1]
    sentence2 = tweets_list[i2]
    total += jaccard_similarity(sentence1, sentence2)
avg_similarity = total / 1000

# Print out the average similarity
print("After 1000 simulations, the average similarity between randomly chosen two tweets is ", avg_similarity)
