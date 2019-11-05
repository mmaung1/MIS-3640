from datetime import datetime
from datetime import date

#create class first 




def days_until_birthday(birthday):
    """How long until my next birthday?"""

    #Ask user for birthday 
    Birthday = input('When is your birthday? [YYYY-MM-DD]: ')
    BIRTH = datetime.strptime(Birthday, '%Y-%m-%d')
    print("Your Birthday is", BIRTH)

    today = datetime.now()
    print("Current date =", today)
    print(datetime.today().strftime('%A'))

    coming_bday = BIRTH.replace(year=today.year)
    print("Your birthday this year:", coming_bday)
    if coming_bday<today:
        coming_bday = coming_bday.replace(today.year+1)
        next = coming_bday - today
        print("Your next birthday is in", next)
    else:
        upcoming = coming_bday - today
        print("your next birthday is",upcoming)
    
    age = today.year - BIRTH.year
    if today.month == BIRTH.month and today.day>=BIRTH.day:
        print('You are: ', age)
    elif today.month < BIRTH.month:
        print('You are: ', age)
    else: 
        print("You are: ", age-1)
    

 

def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    day1=min(b1,b2)
    day2=max(b1,b2)
    diff_days = day2+(day2-day1)
    print(diff_days)

def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week


    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1997, 10, 25)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2017, 12, 25)
    b2 = datetime(2010, 11, 1)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


# def main():
    # datetime_exercises()


if __name__ == '__main__':
    datetime_exercises()
