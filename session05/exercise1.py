import turtle #importing the turtle package
import math  #importing the math package in which we get pi from 
jonathan = turtle.Turtle() #naming the turtle function as jonathan 

print(jonathan) #printing the window
def polygon(turtle, n, length): 
    angle = 360 / n
    for i in range(n):
        turtle.fd(length)
        turtle.lt(angle)

def circle(turtle, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(turtle, n, length)

def arc(turtle, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        turtle.fd(step_length)
        turtle.lt(step_angle)

def triangle (turtle, length, angle):
    for i in range(3):
        turtle.forward(length)
        turtle.left(angle)

def move(turtle,x,y):
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()

# drawing the flower inside the circle 
circle(jonathan, 100) #draw the circle
jonathan.left(60)
arc(jonathan,100,120)
jonathan.left(120)
arc(jonathan,100,120)
jonathan.left(120)
arc(jonathan,100,120)
move(jonathan,0,200)
jonathan.right(59)
arc(jonathan,100,120)
jonathan.left(119)
arc(jonathan,100,120)
jonathan.left(120)
arc(jonathan,100,120)

# #drawing yinyang  
# jonathan.pensize(3)
# circle(jonathan, 100) #draw the circle
# move(jonathan,0,100)
# arc(jonathan,50,180)
# move(jonathan,0,100)
# arc(jonathan,50,180)
# move(jonathan,0,35)
# circle(jonathan,15)
# move(jonathan,0,135)
# circle(jonathan,15)

#drawing the pizza 
# circle(jonathan, 100) #draw the circle
# move(jonathan,54,185)
# jonathan.left(180)
# triangle(jonathan,100,120)
# move(jonathan,-46,12)
# jonathan.right(180)
# triangle(jonathan,100,120)
# move(jonathan,90,48)
# jonathan.left(90)
# triangle(jonathan,100,120)
# move(jonathan,2,99)
# jonathan.left(60)
# triangle(jonathan,100,120)
# move(jonathan,76,122)
# circle(jonathan,29)
# move(jonathan,-40,123)
# circle(jonathan,29)
# move(jonathan,20,66)
# circle(jonathan,29)
# move(jonathan,20,180)
# circle(jonathan,29)




turtle.mainloop() #keeps screen open, but must be at very end

