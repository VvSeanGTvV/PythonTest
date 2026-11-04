#week_10_classes_pt_1
"""Working with dates: classes and functions.

Name: Sean Matthew Gomboc

Fill in each function below. Don't change the function names or parameters:
the test scripts call them exactly as written. Put any code you use to try
things out inside the if __name__ == "__main__": block at the bottom.
"""

from copy import copy


# Part 1:   write the Date class here. Its body only needs a docstring,
#           as with the Time class in the slides

class Date:
  # UNIX values but could also just set 1970 to 1
    year: int = 1970
    month: int = 1
    day: int = 1

    second: int = 0
    pass

# usually this can also be used for anything that is initalizing the class
# def __init__(self, year: int, month: int, day: int):
#   pass

# note: `pass` means "this function doesn't do anything". Remove it when you've
#       written the function.
secondsInDay = 86400 # seconds in a single day
def make_date(year, month, day):
    """Makes a Date object with the given year, month, and day."""
    date = Date()
    try: # Try/Except or the catch, so that it doesn't shuts down the whole operation
        date.year = int(year)
        date.month = int(month)
        date.day = int(day)

        # We need a seconds acting as DATA, but this equation is NOT counting the Leap Years (since it breaks everything due to awkward increment)
        date.second = (int(day) * secondsInDay) + (int(month) * (avg_day_by_month(date) * secondsInDay)) + (int(year) * (get_all_days(date) * secondsInDay))
        fix_format(date)
        return date
    except Exception as e: #failsafe catch
        print(f"Failed to create Date due to: {e}")
        return Date() # use the UNIX default value instead

def date_to_iso(date):
    """Returns the date in ISO form, YYYY-MM-DD, like '2026-03-07'."""
    # Return it as 3 separate variables for an easier task, and its in ISO format
    return str(date.year).zfill(4), str(date.month).zfill(2), str(date.day).zfill(2)


def date_to_us(date):
    """Returns the date in U.S. form, MM/DD/YYYY, like '03/07/2026'."""
    # Reuse the ISO and rearrange the 3 separate variables for an easier task, and its in US format
    year, month, day = date_to_iso(date)
    return month, day, year


def print_date(date):
    """Prints the date in ISO form."""
    year, month, day = date_to_iso(date)
    print(f"{year}-{month}-{day}")


def is_leap_year(year):
    """Returns True if year (an int) is a leap year."""
    if (type(year) is int): # incase whether year is not <int> class
        if (((year / 4) % 2) == 0 or ((year / 4) % 2) == 1): # LEAP by 4
            if (((year / 100) % 2) != 0 and ((year / 100) % 2) != 1): # no LEAP by 100
                return True
            elif (((year / 400) % 2) == 0 or ((year / 400) % 2) == 1): # LEAP by 400
               return True
        return False # Default Value
    else:
        print("input is not <int> class")
        return False # incase whether the year inputted was not an int class


def days_in_month(date):
    """Returns the number of days in the date's month."""
    return month_array(date, True)[date.month - 1] if (date.month - 1) < len(month_array(date, True)) else None


def is_valid(date):
    """Returns True if the date is a real calendar date."""
    return not (days_in_month(date) is None or date.day > days_in_month(date) or date.day <= 0)
    pass


def same_date(date1, date2):
    """Returns True if the two dates have the same year, month, and day."""
    return days_until(today, tomorrow) == 0 # just use the days_until since they calculate by difference between two, and does return 0 when both are same


def is_after(date1, date2):
    """Returns True if date1 comes later on the calendar than date2."""
    return days_until(today, tomorrow) > 0 # same as same_date(...) but now if it is more days than 0


def increment_date(date):
    """Changes the date to the next day. Returns None."""
    date.day += 1 # just increase a day
    fix_format(date)


def next_day(date):
    """Returns a new Date for the day after date. Doesn't change date."""
    new_date = copy(date) # we make a copy and increase a day but never changes the original as we copied its value
    new_date.day += 1
    fix_format(new_date)
    return new_date

def days_until(date1, date2):
    """Returns how many days it takes to get from date1 to date2.

    Assumes date2 is the same as date1 or after it.
    """
    secondsUntil = date2.second - date1.second # Mostly rely on second as technically they are already converted
    return round(secondsUntil / secondsInDay) # Rounds it up to result as Days


# EXTRAS -for convenience sake
def fix_format(date):
    """Fixes the date format to a proper valid date, otherwise throw an error when
    it is unable to fix it."""

    # Added failsafe for sakes it goes over -1
    if (date.day < 1):
        offset = -date.day
        date.month -= 1
        date.day = days_in_month(date) - offset
    
    if (date.month < 1):
        offset = -date.month
        date.year -= 1
        date.month = 12 - offset
        date.day = days_in_month(date) 
    
    if (date.day > days_in_month(date)):
        date.day = 1
        date.month += 1
        
    if (date.month > 12):
        date.month = 1
        date.year += 1

    # reuse the same year limits as 1 - 9999
    if (date.year < 1):
        date.year = 1
    elif (date.year > 9999): 
        date.year = 9999
    
    if (not is_valid(date)):
        fix_format(date)
        #raise ValueError("date no fix err")
    # Update the second for consistency
    date.second = (int(date.day) * secondsInDay) + (int(date.month) * (avg_day_by_month(date) * secondsInDay)) + (int(date.year) * (get_all_days(date) * secondsInDay))

def month_array(date, count_leap: bool = False): # mostly meant for the months in days
    return [31, 29 if (is_leap_year(date.year) and count_leap) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_all_days(date):
    """
    :param date: Only purpose to get the Year for Leap Year checking
    :return: Returns the total Days in a Year
    """
    c = 0
    for i in month_array(date):
        c = c + i
    return c

def avg_day_by_month(date):
    """
    :param date: Only purpose to get the Year for Leap Year checking
    :return: Returns an Average Days (~Day)
    """
    c = get_all_days(date)
    c = c / len(month_array(date))
    return c
    
# Part 3: answer each question in the comments below it.

# Q1. Predict what this prints, then run it to check. Explain the output.
#
#     a = make_date(2026, 2, 28)
#     b = a
#     c = copy(a)
#     increment_date(b)
#     print_date(a)
#     print_date(c)
#     print(a is b, a is c)
#
# A1 Prediction:
# a makes the date of 2026-02-28
# b is now a (or basically any changes to b affects to a)
# c copies a value (meaning c is new value and copies value from a, also doesn't affects a when c is changed)
# b increase the day. (a gets affected from it)
# prints the a's date which is 2026-02-29 (refer back to any change to b affects to a)
# prints the c's date which is 2026-02-28 (as it acts c a new date but copies the value from a)
# prints a is b (which is true), a is c (which is false as c is a new date with a copied value from a)
#
# A1 Explanation:
# basically, since b is same object as a any changes to b affects to a
# but, c is a copy of a (or in hindsight, c is basically a new date w/ copy values of a)
# hence why a is b is true as they are the same object, while a is c is not the same object at all

# Q2. same_date(x, y) can return True while x == y returns False.
#     Give an example and explain why.
#
# A2. Two different object id despite having same value, likewise an example:
# today = make_date(2026, 12, 30) => <__main__.Date object at 0x7e3bd5bd32c0> 
# tomorrow = make_date(2026, 12, 30) => <__main__.Date object at 0x7e3bd5bd32f0>
# Despite being the same date, the object id is not which is why today (x) == tomorrow (y) is false, unless you compared the values inside the date (today, tomorrow) rather than the variable itself
# You could also do the days_until(...) function as techincally it does equal to 0 when they both have same date

# Q3. Someone writes birthday.dya = 15 instead of birthday.day = 15.
#     Python doesn't raise an error. Why not? How would the bug show up later?
#
# A3. Even it despite being an misspelled, it'll create as a new attribute called 'dya'
# than raising an error (cause thats how it works), although if they try getting the "birthday.day"
# since there is no attribute called 'day' it'll result in an error. ('birthday' object has no attribute 'day')
# or it'll just get the attribute 'day' if it exist.

# Q4. days_until should leave date1 unchanged. What would go wrong for
#     the caller if it called increment_date on date1 directly?
#
# A4.


if __name__ == "__main__":
    #UNIX = make_date(1970, 1, 1) <-- this was a temporary test calculation
    today = make_date(2026, 12, 1)
    tomorrow = make_date(2026, 12, 30)
    print_date(today)

    # TESTING FUNCTIONS
    print(is_leap_year(today.year))
    print(days_in_month(today))
    print(days_until(today, tomorrow))
    print(same_date(today, tomorrow))
    print(is_after(today, tomorrow))
    print(is_valid(today))
    increment_date(today)
    print_date(today)
