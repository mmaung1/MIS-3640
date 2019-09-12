##Question 1
import math
print(math.pi)
pi = math.pi #storing pi as variable
print(pi)
r =5 #radius of circle 
v = 4/3*pi*(r**3)
print('The volume of a sphere with radius of 5 is {:.2f}.'.format(v))

##Question 2 
p = 24.95 *0.60 #discounted cover price
s = 3 #shipping cost for 1st book
sc = 59*0.75 # shipping cost for 59 books 
wholesalecost = (p*60)+s+sc
print('The wholesale cost for 60 notebooks is ${:.2f}.'.format(wholesalecost))

##Question 3
# start = (6*60+52)*60 #converting to seconds
# easy =  (8*60+15)*2 #converting to seconds
# normal = (7*60+12)*3 #converting to seconds
# finish_time = (start + easy + normal)/60
# finish_timehrs = finish_time/60
# print('I will get back home in time for breakfast at{:.2f}.'.format(finish_timehrs))
from datetime import timedelta
starttime = timedelta(hours=6, minutes=52)
endtime = starttime + timedelta(minutes=8*2+7*3, seconds=15*2+12*3)
print('I will get back home in time for breakfast at', endtime)

##Question 4
former_grade = 82
new_grade = 89
increase = (new_grade - former_grade)/former_grade #calculating percent increase 
print('My grade increased by {:.1%}.'.format(increase))
