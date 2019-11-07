class Point: 
    """
    represents a point in 2-D space. 
    attributes x, y 
    """
    def __init__(self, x = 10, y =20):
        self.x = x
        self.y = y

    def __str__(self):
        """
        return a point object in a human readable format 
        """
        return f" The x of this point is {self.x} and the y of this point is {self.y}"

    def __add__(self, other):
        new_x = self.x + other.x 
        new_y = self.y + other.y 
        new_point = Point(new_x, new_y) #initialize new point
        return new_point
    
    def __sub__(self, other):
        new_x = self.x - other.x 
        new_y = self.y - other.y 
        new_point = Point(new_x, new_y) #initialize new point
        return new_point
    
    def __eq__(self,other):
        """
        return true if Xs are equal
        """
        return self.x == other.x
    
    def __contains__(self,number):
        """
        check if a number is in a self
        """
        return number == self.x or number == self.y
    

victoria = Point(3,4)
print(victoria)

myat = Point(5,5)

print(victoria+myat)
print(myat-victoria)

carmen = Point(3,6)
print(carmen==victoria) #True
print(carmen==myat) #False

print(3 in victoria) #check whether 3 is in victoria, return true
print(4 in victoria) #true
print(5 in victoria) #false