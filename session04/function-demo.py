def print_lyrics(): #function head/signature, starts with def and must contain paranthesis
    print("Hey Jude. Don't make it bad.") #body of function always indented
    print("Take a sad song and make it better.") # body of function always indented
print_lyrics() #call function by function name with parentheses
print(type(print_lyrics)) #type of variable


def repeat_lyrics():
    print_lyrics() #execute line by line
    print('Na-na-na-na-na-na-na-na-na-na')
    print_lyrics()
repeat_lyrics()


def print_twice(name): #inside the parantheses is caled parameter, and it doesn't mater.
    print(name)
    print(name)
print_twice('Brian') #we are replacing name with Brian, and in the two functions that follow, it is doing the same. 
print_twice('Hey Jude') #we are replacing name with Hey Jude. 
his_name = 'Brian'
print_twice(his_name)

def cat_twice(part1, part2):
    cat = part1 +part2
    print_twice(cat)

cat_twice(100,200) #return as 300 twice because integer
cat_twice('100','200') #return as 100200 twice because string


def give_me_a_break():
    msg = 'break'
    return msg #does not print out the value it returns when the function is called. It however causes the function to exit or terminate immediately, 
    #even if it is not the last statement of the function. whatever after return will not be executed in the function body 
# give_me_a_break()  we don't see what is returned
print(give_me_a_break()) #print function is used to show results


def give_ze_break():
    str1 = 'break'
    print('another break')
    reutrn str1
    print('something else')
print(give_ze_break) # will return line 1 of break, line 2 of another break, will not return something else break will be returned to give_ze_break. 