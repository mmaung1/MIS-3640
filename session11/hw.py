f = open('session09/words.txt')
def word_reader():
    dictionario= dict{}
    for line in f: 
        words=line.strip()
        dictionario[words]=words
    return dictionario


def has_duplicates(f):
    dictionario2 = dict{}
    for listings in f: 
        dictionario2{listings} = 1 + dictionario2.get(listings,0)
        if  dictionario2[listings] > 1:
            return True
    return False 

