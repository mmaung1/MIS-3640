# # def pattern_finder(word): 
# #     i = 0
# #     while i < len(word)-2: 
# #         if word[i:i+2] in word[i+2:]:
# #             return True
# #         i += 1    
# #     return False

# # print(pattern_finder("cdabeab"))
# # print(pattern_finder("zzz"))

# #Question 5 while looop 
# def xyx(word):
#     i = 0
#     while i < len(word)-2:
#         if word[i]==word[i+2]:
#             return True
#         i += 1 
#     return False 

# # print(xyx('abcdefegh'))
# # print(xyx('monkey'))
# # print(xyx('zzz'))
# # print(xyx('azz'))



import math 
import random
def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)

    return the Manhattan distance after n intersections(steps) from the origin
    """
    right_left = x
    backwards_front = y
    for i in range(n):
        direction = random.choice(["front","backwards","left","right"])
        if direction is "right":
            right_left +=1
        elif direction is "left":
            right_left -=1
        elif direction is "front":
            backwards_front +=1
        elif direction is "backwards":
            backwards_front-=1
    distance = abs(right_left-x) + abs(backwards_front-y)
    print(f"The drunkard started from {x} {y}.")
    print(f"After {n} intersections, he's {distance} blocks from where he started.")

drunkard_walk(10,12,9)
