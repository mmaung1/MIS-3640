def most_frequent(string):
    """This function takes a string and prints the letter in decreasing order of frequency
    """
    string = string.replace(" ","") #find spaces of strings and replace with no space
    print(string) #check if it actually works 
    count = {} #create dictionary
    for letter in string: #for each letter in spring
        count[letter] = count.get(letter, 0) + 1
    finalcount = []
    for letter, count in count.items():
        finalcount += [(count, letter)]
    finalcount.sort(reverse=True)
    for count, letter in finalcount:
        print(letter, count)

first = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# most_frequent('I love watching random videos on youtube and that is how I fail to finish python homework')
def anagram_finder(stringhere):
    diccionario =dict()
    for word in stringhere:
        key = ''.join(sorted(word))
        # print(key)
        if key not in diccionario: 
            diccionario[key]=[word]
        else:
            diccionario[key].append(word)
    return diccionario
print(anagram_finder(first))


def printer():
    listanagram = []
    f = open("session09/words.txt")
    for line in f: 
        word = line.strip()
        listanagram.append(word)
    anagrams = anagram_finder(listanagram)
    for key, value in anagrams.items():
        print(key,value)
# printer()

def shortened_printer():
    listanagram = []
    f = open("session09/words.txt")
    for line in f: 
        word = line.strip()
        listanagram.append(word)
    
    listanagram2 = []
    anagrams = anagram_finder(listanagram)
    for key, value in anagrams.items():
        if len(value) > 1:
            listanagram2.append((len(value), value, key))
    listanagram2.sort(reverse=True)
    for word in listanagram2:
        print(word)
print(shortened_printer())

