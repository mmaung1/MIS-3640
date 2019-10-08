def capitalize_all(t):
    result = []
    for word in t:
        result.append(word.capitalize())
    return result 

names = ['nico', 'myat', 'carmen', 'vicky']
print(capitalize_all(names))

def only_upper(t):
    res =[]
    for s in t:
        if s[0].isupper():
            res.append(s)
    return res

name = ['Jinna', 'SHUAN', 'JENNY', 'Brian', 'julie', 'shirley']

print(only_upper(name))