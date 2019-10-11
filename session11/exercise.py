# def histogram(s):
#     d = dict()
#     for letter in s: 
#         if letter not in d:
#             d[letter] = 1 #you are counting, so this is the first letter so the value one
#         else:
#             d[letter] +=1 #it already exists, so you are adding one. 1+1 =2
#         print(d)
#     return d   #you got to finish the for loop and return d 

# h=histogram('bookkeeper')
# print(h)



# with open('session11/she_loves_you.txt') as f:
#     lyrics = f.read().split()
#     print(lyrics)

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d: 
#             d[c]=1
#         else:
#             d[c]+=1
#     return d 

# def print_hist(h):
#     for c in h: 
#         print(c,h[c])

# beatles = histogram(lyrics)
# print_hist(beatles)


  
import urllib.request
import json
 
url = "http://api.open-notify.org/astros.json"
 
with urllib.request.urlopen(url) as f:  
    response_text = f.read().decode('utf-8')
    j = json.loads(response_text)
    print(j)
    
    # Can you print number of people in the space?

    # Can you print all the names?
# print(len(j))
# print(j['number'])
print(j['people']) #print the list of 

for person in j['people']:
    print(person['name'] 'is in' person['craft'])

