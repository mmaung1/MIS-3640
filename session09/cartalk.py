f = open('session09/words.txt')
#numerouno
def triple_threat(word):
    for i in range(len(word)-5): #without the -5, you're getting index out of bound, e.g: string = 'hellomyat' only have indices 0 to 8 but we have 8+5 in code
        if word[i]== word[i+1]:
            if word[i+2]==word[i+3]:
                if word[i+4]==word[i+5]:
                    return True       
    return False

def searcher():
    for line in f:
        word = line.strip()
        if triple_threat(word):
            print(word)
searcher()


# #numerodos
# def agefinder():
#     for i in range(1,100):
#         age = str(i)
#         if
