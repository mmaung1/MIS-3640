import time
time.time()
currentdate = int(time.time())
print(currentdate)
days = currentdate//3600//24 #divide the seconds by seconds in an hour, then # of hours in a day 
print(days)
print('It has been', days, 'days since the epoch.')

midnight_currentdate = days*24*3600 #calculate to get the seconds at midnight of the days 
print(midnight_currentdate)
seconds_since_midnight  = currentdate - midnight_currentdate #calculate the seconds difference from midnight at current date and current date's time. 
print(seconds_since_midnight)
hours = seconds_since_midnight//3600 #calculate hours of the day by dividing number of seconds in an hour and rounding up 
print(hours)
minutes = (seconds_since_midnight - (hours*3600))//60  #calculate minutes of the day by difference b/w seconds since midnight and seconds of the day, then divide by 60
print(minutes)
seconds = seconds_since_midnight - (hours*3600 + minutes*60) # calculate seconds of the day by difference b/w seconds since midnight and seconds of day 
print(seconds)
time_of_day = "%s:%s:%s" % (hours,minutes,seconds) 
print(time_of_day)
print(time_of_day,"on", days, "days since epoch")

print (time.gmtime(currentdate))


