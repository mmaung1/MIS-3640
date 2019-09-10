# print('Please enter your name here:')
# name = input('Please enter your name here:')
# print('Hello', name)
# message = 'I did something incredible today!'
# n = 100
# pi = 3.14
# strings work with plus signs but not with minus signs
# print('2'+'1')

# first_name = 'John'
# last_name = 'Lennon'
# print('Hello' +' ' + first_name+' '+last_name+' '+'.')

# firstname= (input('Please enter your first name here:'))
# lastname = (input('Please enter your last name here:'))
# fullname = firstname + ' '+ lastname
# print('Hello'+' '+fullname+'!')

# print('Pi equals {:.5f}.'.format(3.141592653589793))
# 5 means keep the 5 decimal spaces when we keep, . means keep the ., f means floating number, not integer 

# print('Age: {age}; Gender:{sex}'.format(sex='Female', age=20))
# print('Age:{} Gender{}'.format('Female',20))
# f is a new data type, it is not a pure string, it contains a variable in it, but the variable must be contained in {}
sex = 'Female'
age = 20

print(f'Age: {age}; Gender: {sex}')
print('Age:{age}; Gender: {sex}'.format(sex=sex, age=age))