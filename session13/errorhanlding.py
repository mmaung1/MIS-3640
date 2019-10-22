# try:
#     number = int(input('Please enter a number: '))
#     result = 2019/number
#     print(result)
#     name = 'Babson'
#     print(name[number])
# except ZeroDivisionError as e: #this e can be anything, its just a name, like a too 
#     print('Something is wrong:',e)
# except ValueError as e:
#     print('THere is a value Error:',e)
# except IndexError as e:
#     print('There is an Index Error:',e)
# else: 
#     print('This is in else')

# print('After something is wrong, we still can get here')




def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k 
    raise LookupError()
name_dict = {'Shaun':90,'Brian':80, 'Victoria':85}
print(reverse_lookup(d=name_dict,v=100))