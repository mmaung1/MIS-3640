import turtle
import math
brian = turtle.Turtle()

print(brian)
#for i in range(4): #you don't care about what i is, you just need to put something b/w for and in. it's just a name
#   brian.fd(100)
#   brian.lt(90)

# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
# square(brian, 200)



# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)
# polygon(brian, 200, 3)

# def arc(t,r,angle):
#     arc_length = 2*math.pi*r*angle/360
#     n = int(arc_length/3)+1
#     step_length = arc_length/n
#     step_angle = angle/n
#     polyline(t,n, step_lenght)
    
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)
# arc(brian,100,90)


def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,n,length):
    angle = 360/n 
    polyline(t,n,length,angle)

turtle.mainloop()


# def move(t,x,y):
#     t.pu()
#     t.setpos(x,y)
#     t.pd()

# arc(brian, 100, 360)
# move(brian, 300, 100)
# polygon(brian, 3, 100)

# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = 50
#     length = circumference / n
#     polygon(t, n, length)
# turtle.mainloop()