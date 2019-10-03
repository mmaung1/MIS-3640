# print('Hello, World!')
# print('Hey Jude, don\'t make it bad')
# print('The total number of overall medals in Rio is', 46 + 48 +37)
# name = input()
# print(name)
# print('Hello' name)

# x = 10
# print(x)
# x = x+2
# print(x)

# a = 'ABC' 
# b = a
# a = 'XYZ'
# print(b)

# print('Hello,{}'.format('world'))
# print('Congratulations,{:s}, you won the {:d}th Academy Award.'.format('Gary Oldman',90))

# print('Pi equals {:.5f}'.format(3.1415926))
# print('Age is {}. Gender is {}'.format(20,'female'))
# print('Growth rate is {:.2f}%'.format(8))
# print('Coordinates are {long} and {lang}'.format(long='420.5', lang= '530'))
# print('Coordinates are {1},{0},{2}'.format('5','8','10'))

# print('What is the volume of a sphere with radius 5')
# radius = int(input('What is the radius?'))
# pi = 3.14
# volume = (4/3)*pi*radius**3
# print('Volume of the sphere with radius 5 is{:.2f}'.format(volume))

# coverprice = 24.95*0.6*60
# shipping1 = 3 + 0.75*59
# total = shipping1 +coverprice
# print('The total cost of the books is {:.2f}'.format(total))

# percent_increase = (89-82)/82*100
# print('The percentage increase is {:02.1f}%'.format(percent_increase))


# # print(len(str(2**1000000))) #find out how many digits in this number
# print('I\'m Learning \nPython') #n returns onto next line
# print('\\\n\\')
# print(r'\\\t\\') #r' avoids the backward slash (escape) character
# print('''line 1  
# ...line 2          
# ...line 3''') #''' breaks the lines
# print(3>2) #will print true because 3 is bigger than 2
# print(2>3) #will print false because 2 is not bigger than 3

# print(2<3) and print(5>4)


# def area(r):
#     pi = 3.14
#     volume = pi*r*r
#     return volume
# print(area(11.55))

# def print_lyrics():
#     print("Hey Jude. Don\'t make it bad")
#     print("Turn a sad son make it better")
# print_lyrics()

# def remix():
#     print_lyrics()
#     print("DJ Khaled Remix")
#     print_lyrics()
# remix()

# def print_twice(whatever_name):
#     print(whatever_name)
#     print(whatever_name)

# myname='Jack'
# print_twice(myname)

# import math

# def absolute(number):
#     number = int(number)
#     if number >= 0:
#         print(number)
#     else:
#         print(-number)
# absolute(-4)

# def brian_abs(number):
#     if isinstance(number, int):

#         if number >= 0:
#             return number
#         else:
#             return -number
#     else:
#         return 'I don\'t know'
# print(brian_abs(-8))

# def absolute(number):
#     if isinstance(number, int): #this transforms number into int
#         if number >=0:
#             return number
#         else: 
#             return -number
# print(absolute(-4))


# def give_me_a_break():
#     str1 = 'break'
#     return str1
# print(give_me_a_break())


# def quadratric(a,b,c):
#     x1= -b +((b**2-4*a*c)**0.5)/(2*a)
#     x2= -b -((b**2-4*a*c)**0.5)/(2*a)
#     print('The answers are {:.2f} and {:.2f}'.format(x1,x2))
# quadratric(40,12,8)


# import turtle 
# jack = turtle.Turtle() #name it under jack 
# print(jack)
# jack.fd(100)
# turtle.mainloop()

# age = 20 #assignment statement
# if age >= 18:
#     print('You are an adult')
# else:
#     print('Still a child')

# age = 3 
# if age >= 5:
#     print('You are', age,'and an adult.')
# else:
#     print('You are', age,'and a child.')

# age = 60
# if age>=0 and age <10:
#     print('You are', age, 'a child')
# elif age>=11 and age<13:
#     print('You are', age, 'a kid')
# elif age>14 and age<19:
#     print('You are',age,'a teenager')
# else:
#     print('You are',age,'an old person')

# x = 5
# y = 6
# if x==y:
#     print('x and y are equal')
# else:
#     if x < y: 
#         print('X is less than y')
#     else:
#         print('X is more than y')


# def bmicalculator(weight, height):
#     bmi = (weight)/(height**2)
#     if bmi < 18.5:
#         print ('You are underweight')
#     elif bmi >= 18.5 and bmi <= 24.9:
#         print ('You have normal BMI')
#     elif bmi >=25 and bmi <=29.9:
#         print('You are overweight')
#     elif bmi >30:
#         print('You are obese')
# bmicalculator(50,1.4)


# def valuefinder(varA,varB):
#     if isinstance(varA, str) or isinstance(varB,str):
#         print('String Involved')
#     elif varA > varB:
#         print('bigger')
#     elif varA == varB:
#         print('equal')
#     elif varA < varB:
#         print('smaller')
# valuefinder(42,49)

# def countdown(n):
#     if n <= 0:
#         print('blastoff')
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5) #if we don't call the function, it will just be stored within 
#here because it is a will keep running the second condition if the value is not 0 until it meets the 'if' condition, then it will print blastoff

# def print_n(s,n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s, n-1) #this prints s n-1 times.
# print_n(4,7)

# result = 0
# for i in range(1,20,2):
#     result += i
# print(result)

# result = 0 
# for i in range(1,11,1):
#     result +=i
# print(result)

# result = 0 
# for i in range(1,1001,1):
#     result +=i
# print(result)

# result = 0 
# for i in range(1,1001,2):
#     result +=i
# print(result)

# result = 0 
# for i in range(1,1001):
#     result += i*i
# print(result)

# def countdown(n): 
#     while n>0:
#         print(n)
#         n = n-1 
#     print('Blastoff!')
# countdown(8)

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count = count + 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 
# #in here at it 0, count 0 + 12 = 12, it 1, count stored as 12 + 12= 24 and so on\\iteration = 0

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
#count will be always 12 because, count variable is defined within the loop and is reset to 0 with each iteration

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 7:
        break
print(mysum)


"""
Question 1:
If the number, n, is divisible by 4, return True; return False otherwise.
Return False if n is divisible by 100 (for example, 1900); the only exception is when n is divisible by 400(for example, 2000), return True.
"""


def is_special(n):
    """
    If the number, n, is divisible by 4 (for example, 2020), return True.
    Return False if n is divisible by 100 (for example, 300); the only exception is when n is divisible by 400(for example, 2400), return True.
    """
    if n%4 == 0:
        if n%100 == 0:
            if n%400 == 0:
                return True
            return False
        return True
    else:
        return False


# When you've completed your function, uncomment the
# following lines and run this file to test!


print(is_special(2020))
print(is_special(300))
print(is_special(2018))
print(is_special(2000))

"""
-----------------------------------------------------------------------
Question 2:
"""


def detect(a, b, n):
    """
    Returns True if either a or b is n, or if the sum or difference or product of a and b is n. 
    """
    if a == n or b == n or a+b == n or abs(a-b) == n or a*b == n:
        return True
    else:
        return False


# When you've completed your function, uncomment the
# following lines and run this file to test!

print(detect(2018, 9, 2018))
print(detect(2017, 1, 2018))
print(detect(1009, 2, 2018))
print(detect(2020, 2, 2018))
print(detect(2017, 3, 2018))

"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes the sum of all cubes of all the odd numbers between 1(inclusive) and n (inclusive if n is not even).
"""


def sum_cubes_of_odd_numbers(n):
    sum = 0
    if n%2 == 0:
        for i in range(1, n):
            if i%2 == 1:
                sum += i**3
    else:
        for i in range(1, n+1):
            if i%2 == 1:
                sum += i**3
    return sum


# When you've completed your function, uncomment the
# following lines and run this file to test!

print(sum_cubes_of_odd_numbers(1))
print(sum_cubes_of_odd_numbers(10))