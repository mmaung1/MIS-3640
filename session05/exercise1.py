import turtle #importing the turtle package
import math  #importing the math package in which we get pi from 
jonathan = turtle.Turtle() #naming the turtle function as jonathan 

print(jonathan) #printing the window
def polygon(t, n, length): 
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def move(t,x,y):
    t.pu()
    t.setpos(x,y)
    t.pd()

#drawing the flower inside the circle 
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

turtle.mainloop() #keeps screen open, but must be at very end

