# fin = open("session09/words.txt")
# line = fin.readline()
# word = line.strip()
# print(word)

# for line in fin:
#     word = line.strip()
# print(word)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open("session09/words.txt")
    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    for letter in word:
        if letter == "e" or letter == "E":
            return False
    return True


# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open("session09/words.txt")
    num_words_no_e = 0
    num_of_words = 0
    num_words_with_e = 0
    for line in f:
        num_of_words += 1
        word = line.strip()
        if has_no_e(word):
            # print(word)
            num_words_no_e += 1
        else:
            num_words_with_e += 1
    return num_words_no_e / num_of_words


# print( 'The percentage of the words with no "e" is {:.2f}%.'.format(
#         find_words_no_e() * 100
#     ) )


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True
    

# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't vowel letters
    """
    f = open("session09/words.txt")
    num_words_no_vowel = 0
    num_of_words = 0
    for line in f:
        num_of_words += 1
        word = line.strip()
        if avoids(word, 'aeiou'):
            # print(word)
            num_words_no_vowel += 1
    return num_words_no_vowel / num_of_words



# print('The percentage of the words without vowel letters is {:.2f}%.'.format(
#     find_words_no_vowels()*100))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))

def find_words_only_use_planet():
    f = open('session09/words.txt')
    num_words_only_use_plane = 0
    for line in f:
        word = line.strip()
        if uses_only(word, 'planet'):
            num_words_only_use_plane +=1
            print(word)
    return num_words_only_use_plane

# print('Number of words that use only letters from "planet" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    # for letter in required:
    #     if letter not in word:
    #         return False
    # return True
    return uses_only(required, word)


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))
# print(uses_all('Babson', 'aeoiu'))
# print(uses_all('Babesonious', 'aeoiu'))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open('session09/words.txt')
    num_words_use_all_vowels = 0
    for line in f:
        word = line.strip()
        if uses_all(word, 'aeiou'):
            num_words_use_all_vowels +=1
            print(word)
    return num_words_use_all_vowels


# print('The number of words that use all the vowels:',
#       find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    left = word[0]
    for letter in word:
        if left > letter[1:]:
            return False
        left = letter
    return True


print(is_abecedarian('abs'))
print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words and the longest abecedarian word
    """
    fin = open('session09/words.txt')
    abecedarian = []
    longest_word = ""
    longest = 0
    counter = 0
    for i in fin:
        word = line.strip()
        if is_abecedarian(word):
            abecedarian.append(word)
            counter += 1
    for word in abecedarian:
        if len(longest_word)<len(word):
            longest_word = word
            longest = len(word)
    print(f"There's {counter} abecedarian words, and the longest word is {longest_word}")

find_abecedarian_words()


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    if len(word) <=1:
        return True 
    elif ord(word[1]) < ord(word[0]):
        return False
    else:
        return is_abecedarian_using_recursion(word[1:])


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    while len(word) > 1:
        if ord(word[1]) < ord(word[0]):
            return False
        word = word[1:]
    return True