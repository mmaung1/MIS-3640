itemslist = ['bananas','rice','paprika','potato chips']

def pricecalculation(price):
    price_point = 0  #store price point as 0 for variable
    for c in price:   #for every letter in the variable price
        price_point += float(ord(c)) - 96 #store again under price_point, as integer converted from ord - 96
    return price_point

def totalcalculation(item):
    final = 0 
    for i in item:
        final += pricecalculation(i)
    for i in item: 
        print(i, "$ {:02.2f}".format(pricecalculation(i)))
    print('---------------')
    print("The total is $ {:02.2f}".format(final))

totalcalculation(itemslist)


# #exercise 5
# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False

# print(any_lowercase1('LOLo'))

# #The function only checks whether the first letter of the string is lowercase or not, it doesn't take into consideration the following letters. 
# #If the function detects that 1st letter is lowercase, true is returned, else false is returned.


# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'


# #The function will only check if 'c' in the if statement is lowercase. Because 'c' is a fixed  value, the function will always output True



# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag


# #It checks if s has any lowercase values any lowercase values, however because python reads left to right, so if the last letter is upper case, it will return false, but if it is lowercase. will return true.


# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag


# #checks if there are any lowercase in string and returns false

# def any_lowercase5(s):
#     for c in s:
#         if not c.islower():
#             return False
#     return True

# #Checks whether or not the s is lowercase and If any letter is capital it will return FALSE.


