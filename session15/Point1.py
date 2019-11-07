import math


class Point: #by using class, we are defining new type, point. 
    """Represents a point in 2-D space.

    attributes: x, y
    """

my_point = Point() #this is creating an object 
# print(my_point)
# print(type(my_point))
# print(my_point.__doc__) #prints out docstring
my_point.x=3.0 #storing attributes
my_point.y=4.0 #storing attributes
print(my_point.x,my_point.y)



def print_point(p):
    """Print a Point object in human-readable format."""
    print(f'({p.x}, {p.y}).')

print_point(my_point)
print(hasattr(my_point,'x')) #check if there is attribute x, true
print(hasattr(my_point,'y')) #check if there is attribute y, true 
print(hasattr(my_point,'z')) #check if there is attribute z, false
print(dir(my_point))


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    diff_x = p2.x - p1.x 
    diff_y = p2.y - p1.y
    d = math.sqrt(diff_x**2 + diff_y**2)
    return d


myat_point = Point() #create object myat in point 
myat_point.x, myat_point.y = 6,8 #store x and y respectively 
# # myat_point.x = 6
# # myat_point.y = 8
print(myat_point.x,myat_point.y) #print x and y 
print(distance_between_points(my_point, myat_point)) #print the distance between my_point and myat_point 

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

box = Rectangle() #how we create a rectangle object 
box.width = 100.0
box.height = 200.0
box.corner = Point() #creating a new point for your corner but you can call back to previous point 
box.corner.x = 0
box.corner.y = 0 
print(distance_between_points(my_point,box.corner)) #print distance between that corner and my point 



def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

center_of_box = find_center(box) #this will take all the attributes of the box and run it thru this function and find center
print_point(center_of_box) #will print out the center point of the box 


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight
    return rect.width and rect.height
print(grow_rectangle(box, 100,100)) #take the box attributes and add it ont 


def print_rectangle(rect):
    """
    prints the width and height and lower - left corner of the given Rectangle object.
    """
    print(f'width: {rect.width}, height:{rect.height}')
    print('the lower-left corner:')
    print_point(rect.corner)
print_rectangle(box)
grow_rectangle(box,100,100)
print("after growing...")
print_rectangle(box)


def main():
    my_point = Point()
    print(Point.__doc__)
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    print('Is my_point an instance of Point?', isinstance(my_point, Point))
    print('Is my_point an instance of Rectangle?',
          isinstance(my_point, Rectangle))
    print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print('Does box have an attribute x?', hasattr(box, 'x'))

    print('Does box have an attribute corner?', hasattr(box, 'corner'))

    print('Rectangle has these:', dir(box))

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


if __name__ == '__main__':
    main()
    # p1 = Point()
    # p1.x = 3
    # p1.y = 4 

    # import copy 
    # p2 = copy.copy(p1) #trying to get everything that p1 has and put it on p2 
    # print_point(p1)
    # print_point(p2)
    # print(id(p1))
    # print(id(p2))
    # print(p1 is p2) #false tho
    # print(p1.x is p2.x) #True, because usually small integers are in same location 
    # print(p1==p2) #false because 
    # print(dir(p1)) 
