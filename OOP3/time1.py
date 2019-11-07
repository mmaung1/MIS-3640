class Time: 
    """
    Represent the time of day. 
    
    attributes: hour, minute, second 
    """
    #1st thing - provides values to the attributes; an initializer
    def __init__(self, hour=0, minute=0, second=0): #setting the default values
        self.hour = hour #left hand side is the attribute of the object, rhs is argument, lhs belongs to Time()
        self.minute = minute
        self.second = second 
    
    def __str__(self):
        """
        return a time object in a human readable format 
        text represnetation of this object
        """
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __add__(self,other):
        seconds = self.time_to_int

    def print_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
    
    def time_to_int(self):
        minutes = self.hour * 60 +self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def is_after(self, other):
        return self.time_to_int()>other.time_to_int()
    
    def increment(self, seconds):
        result = Time(3,0,0)
        result.hour = self.hour
        result.minute = self.minute
        result.second = self.second 

        result.second += seconds
        
        if result.second >= 60:
            result.minute +=1
            result.second -=60


        if result.minute >= 60:
            result.hour +=1
            result.minute -= 60
        return result


start = Time(3, 0, 0) #initialize the time object 
# start.hour = 3
# start.minute = 11
# start.second = 30

start.print_time() #start owns the method 
print(start.time_to_int()) #since it returns something, you need to print it

end = start.increment(100)
end.print_time()
print(end.is_after(start))

now = Time(3,36,0)  #Time() is a contstructor, creating a Time Object, with flexibility 
              # It will call the init function 
now.print_time()

time_2 = Time(minute = 30, second=5) #the following will print 00:00:00 since the default is 0 
time_2.print_time()