# Import Halloween vocabulary word list

def read_file_to_list(path_to_file):
    """
    reads file of words, return a list of words
    """
    f = open(path_to_file)
    words = []
    for line in f:
        word = line.strip()
        words.append(word)
    return words

read_file_to_list("assignment2/halloween_word_list.txt")

"custom"
"party"
"pumpkin"
"joker"
"horror"