# team = 'New England Patriots' #each element is a character in the string, including the spaces, digits, signs 
# letter = team[0]
# print(letter) #will print N, because python starts from 0
# print(team[1])
# # print(team[1.5]) index is always an integer 
# #we always start any sequence, string, lengths from 0.
# print(len(team)) #counts the number of characters in variable
# print(team[-1]) #prints s 
# print(team[-20]) #prints N 

team = 'New England Patriots'
# print(team[20])
# index = 0 
# while index < len(team):
#     letter =team[index]
#     print(letter)
#     index = index +1 

# for letter in team: 
#     print(letter) 

# prefixes = 'JKLMNOPQ'
# suffixes = 'ack'
# for letter in prefixes: 
#     if letter=='O' or letter=='Q':
#         print(letter + 'u' + suffixes)
#     else:
#         print(letter + suffixes)


# team = 'New England Patriots'
# print(team[:11]) #from beginning to 11
# print(team[12:]) #from 12 to end 
# print(team[0:20:2])
# print(team[::2])

# # team[12:20]= 'Seahawks'
# new_team = team[:12] + 'Giants'
# print(new_team)
# print(team)

team = 'New England Patriots'
def count(s, letter):
    counter = 0 
    for c in s: 
        if c == letter:
            counter = counter +1 
    return counter

print(ord('a'))
print(count(team,'e'))

