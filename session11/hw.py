# f = open('session09/words.txt')
# def word_reader():
#     dictionario= dict{}
#     for line in f: 
#         words=line.strip()
#         dictionario[words]=words
#     return dictionario


# def has_duplicates(f):
#     dictionario2 = dict{}
#     for listings in f: 
#         dictionario2{listings} = 1 + dictionario2.get(listings,0)
#         if  dictionario2[listings] > 1:
#             return True
#     return False 


def create_dict():
    words ={}
    f = open('session09/words.txt')
    for line in f:
        # print(line)
        word = line.strip()
        # print(word)
        words[word] = 0
    return words
words_dict = create_dict()

# for w in words_dict:   ##prints all the values and keys in a dict
#     print(w, words_dict[w])

# for w,v in words_dict.items(): # #prints all values and keys in dict
#     print(w,v)


def check_word(word,d):
    return word in d


if __name__=="__main__":
    words_dict = create_dict()
    # for w in words_dict:   ##prints all the values and keys in a dict
#     print(w, words_dict[w])
# for w,v in words_dict.items(): # #prints all values and keys in dict
#     print(w,v)
    word = input('Enter a word:')
    if check_word(word,words_dict):
        print(f'Yes, the word {word} is in dict')
    else:
        print(f'SOrry the word {word} is not here.')


