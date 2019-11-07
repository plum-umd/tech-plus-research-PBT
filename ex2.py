# From https://medium.com/russell-duhon/property-based-testing-from-scratch-in-python-bb1a8b56daf6

import datetime
import calendar
from hypothesis import given, settings
from hypothesis.strategies import dates

def twenty_first(birthday):
    # compute the number of leap years up to birthday
    leapdays = calendar.leapdays(birthday.year, birthday.year + 22) 
    if calendar.isleap(birthday.year) and birthday.month > 2:
        leapdays -= 1
    elif calendar.isleap(birthday.year + 1) and birthday.month < 3:
        leapdays -= 1
    # include this value when computing the result
    return birthday + datetime.timedelta(days=365 * 21 + leapdays)

''' 
To find the bug, you may want to restrict the dates that can be generated:

    @given(dates(min_value=datetime.date(1950, 1, 1), max_value=datetime.date(2050, 12, 31)))
    
Or increase the number of inputs tested:

    @settings(max_examples=1000)
'''
@given(dates())
def test_must_be_in_same_month(birthday):
    error_message = """{} doesn't have the right twentyfirst birthday!
        Instead it has {}""".format(birthday, twenty_first(birthday))
    assert birthday.month == twenty_first(birthday).month, error_message