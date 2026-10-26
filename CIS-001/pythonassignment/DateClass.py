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
    pass

# usually this can also be used for anything that is initalizing the class
# def __init__(self, year: int, month: int, day: int):
#   pass

# note: `pass` means "this function doesn't do anything". Remove it when you've
#       written the function.
def make_date(year, month, day):
    """Makes a Date object with the given year, month, and day."""
    date = Date()
    try: # Try/Except or the catch, so that it doesn't shuts down the whole operation
        date.year = int(year)
        date.month = int(month)
        date.day = int(day)
        return date
    except Exception as e:
        print(f"Failed to create Date due to: {e}")
        return None


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
    pass


def is_valid(date):
    """Returns True if the date is a real calendar date."""
    pass


def same_date(date1, date2):
    """Returns True if the two dates have the same year, month, and day."""
    pass


def is_after(date1, date2):
    """Returns True if date1 comes later on the calendar than date2."""
    pass


def increment_date(date):
    """Changes the date to the next day. Returns None."""
    pass


def next_day(date):
    """Returns a new Date for the day after date. Doesn't change date."""
    pass


def days_until(date1, date2):
    """Returns how many days it takes to get from date1 to date2.

    Assumes date2 is the same as date1 or after it.
    """
    pass


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
# Prediction:
# Explanation:

# Q2. same_date(x, y) can return True while x == y returns False.
#     Give an example and explain why.
#

# Q3. Someone writes birthday.dya = 15 instead of birthday.day = 15.
#     Python doesn't raise an error. Why not? How would the bug show up later?
#
# A3. Even it despite being an misspelled, it'll create as a new attribute called 'dya'
# than raising an error (cause tahts how it works), although if they try getting the "birthday.day"
# since there is no attribute called 'day' it'll result in an error. ('birthday' object has no attribute 'day')

# Q4. days_until should leave date1 unchanged. What would go wrong for
#     the caller if it called increment_date on date1 directly?
#


if __name__ == "__main__":
    today = make_date(2026, 10, 26)
    print_date(today)
    print(is_leap_year(today.year))
