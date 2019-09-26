# age = int(input('Please enter your age:'))
# print(f'Your age is {age}.')
# if age>=18:
#     print('You are an adult.')
# elif age<=12:
#     print('You are a child.')
# else:
#     print('You are a teenager.')

#after if and elif, you always need a condition, but in else you dont need a condition, will always go to the first condition. 


# def bmi_calculator(height,weight):
#     bmi= (703*weight)/(height*height)
#     print(f'Your BMI is {bmi}.')
#     if bmi <= 18.5:
#         print('You are underweight')
#     elif bmi >= 18.5 and bmi <=24.9:
#         print('You have a normal BMI')
#     elif bmi >=25 and bmi <=29.9:
#         print('You are overweight.')
#     else:
#         print('You are obese')
# bmi_calculator(60,113)


# def compare(a,b):
#     if isinstance(a, str):
#         print('a has a string involved')
#     elif isinstance(b,str):
#         print('b has a string invovled')
#     else:
#         if a > b:
#             print('a is bigger than b')
#         elif a == b:
#             print('a and b are equal')
#         else:
#             print('b is bigger than a')

# compare(52,42) #string involved 

# """
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21."""

# def diff21(n):
#     if n <=21:
#         return abs(21-n)
#     else: 
#         return abs(n-21)*2

# print(diff21(19)) #expecting 2
# print(diff21(10)) #expecting 11
# print(diff21(21)) #expecting 0


# def countdown(n):
#     import time
#     time.sleep(1)
#     if n<= 0: 
#         print("Blastoff")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)