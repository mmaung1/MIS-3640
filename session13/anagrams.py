def read_file_to_list(path_to_file):
    """
    reads file of words, returns a list of words
    """
    f = open('session09/words.txt')
    words = []
    for line in f: 
        word = line.strip() 
        words.append(word)
    return words


def list_to_dict(words):
    """
    convert a list of words to a dictionary and return it 
    the dictionary should be like: 
    {'aedlts':['deltas','desalt','lasted','slated','salted','staled']}
    """
    d = {}
    for word in words: 
        fingerprint = ''.join(sorted(word))
        # print(type(word),word)
        # print(type(fingerprint),fingerprint)
        if fingerprint not in d: 
            d[fingerprint] = [word]
        else:
            d[fingerprint].append(word)
    return d


def print_anagrams(word_dict, nwords = 1): 
    """
    prints all the anagrams with more than one word
    """
    for v in word_dict.values(): 
        if len(v)>nwords:
            print(v)
# words_list = read_file_to_list() 

# anagrams is a dictionary 
# {'aedlts':['deltas','desalt','lasted','slated','salted','staled']}

def create_new_dict(old_dict):
    """
    create a new dictionary, key is the number, value is the anagrams with the same number of words 
    return the new dictionary 
    """
    d = dict()
    for v i in old_dict.values():
        k = len(v)
        if k not in d: 
            d[k]=[v]
        else:
            d[k].append(v)
    return d 



def print_dict_this_way():
    """
    words_dict is a dictionary with integer:  list of word lists pairs 
    """
    for k in sorted(words_dict.key(),reverse = True):
        print(words_dict[num])


def main():
    words_list = ['deltas','retainers','desalt','lasted','salted','slated','ternaries','greatening','brian']
    # path_to_words_file = "session09/words.txt"
    # words_list = read_file_to_list(path_to_words_file)
    # print(len(words_list))
    # print(words_list[:20])
    # print(words_list[:-20])
    anagrams = list_to_dict(words_list)
    print_anagrams(anagrams, nwords=3)
    new_dict = create_new_dict(anagrams)
    #print the dictionary 
    print_anagrams_this_way(new_dict)

if __name__=="__main__":
    main()