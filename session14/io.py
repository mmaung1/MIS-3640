# f_out = open('session14/output.txt', 'w') #w means its for writing, if we run this nothing is gonna happen except one file will be created in session14

# line1 = 'How many roads must a man walk down\n'

# f_out.write(line1) #write method will write the line1 onto output.txt 
# #everytime we do this, it will overwrite old one 

# line2 = 'Before you call him a man?\n'
# f_out.write(line2)
# f_out.close

import os
# print(os.getcwd())

# with open('session14/output.tct','w') as f_out: 
#     line1 = 'How many roads must a man walk down\n'
#     f_out.write(line1) #write method will write the line1 onto output.txt 
#     #everytime we do this, it will overwrite old one 
#     line2 = 'Before you call him a man?\n'
#     f_out.write(line2)



# print(os.path.abspath('output.txt'))
# print(os.path.exists('session14/output.txt'))


# def walk(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)

# walk(os.getcwd()) #print all the files under current working directory 


# f_in = open('bad_file') #this is going to cause error because no such file exists 
# try: 
#     f_in = open('bad_file')
# except FileNotFoundError as e:
#     print('something is wrong', e)


import dbm # built in data base module in python, looks just like dictionary 
import random 


import pickle 
t = [1,2,{'Carmen':95, 'Victoria':99}]

with open('saved.p','wb') as p: #the file must be in bytes because we are writing in bytes  
    pickle.dump(t, p) 
# print(pickle.dumps(t)) #dumps returns pickled representation of object as a bytes object (returns pickled representation of t )

with open('saved.p','rb') as p:
    t2 = pickle.load(p)

print(t2)
print(t==t2)
print(t is t2)
