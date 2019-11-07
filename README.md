# tech-plus-research-PBT
Tech + Research project for property-based testing in Python

## Exercises

We've written a few example programs to help get you started. The first two explain how to use pytest and Hypothesis, but the last example doesn't have any testing code built in. It's your job to find the bugs!

# Exercise 1

*Adapted from this [blog post](https://www.freecodecamp.org/news/intro-to-property-based-testing-in-python-6321e0c2f8b/).*

Say that we want to write a function that adds two numbers (there is an obvious way to do this, but let's ignore that for now).
We come up with the following test cases:
* sum(3,5) = 8
* sum(-2,-2) = -4
* sum(-1,5) = 4
* sum(3,-5) = -2
* sum(0,5) = 5
With these test cases, the following code seems ok.
```python
def sum(num1, num2):
    if num1 == 3 and num2 == 5:
        return 8
    elif num1 == -2 and num2  == -2:
        return -4
    elif num1 == -1 and num2 == 5:
        return 4
    elif num1 == 3 and num2 == -5:
        return -2
    elif num1 == 0 and num2 == 5:
        return 5

```

We can test our code using pytest as follows:
```python
import pytest

@pytest.mark.parametrize('num1, num2, expected',[(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)])
def test_sum(num1, num2, expected):
    assert sum(num1, num2) == expected
```
When you run this, you should see that all tests pass.

But that's not really what we wanted.
We want a function that correctly adds *any* pair of numbers, not just the five pairs we tested.
So let's write a more general property-based test using Hypothesis:
```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_sum(num1, num2):
    assert sum(num1, num2) == num1 + num2
```

As you might have expected, this test will fail.

It's easy to test our sum function for correctness because there is a built-in operation that does what we want (+).
In general, we may have to test for correctness indirectly.
For example, we may want to check that our implementation of sum is commutative.
```python
from hypothesis import given, settings, Verbosity
import hypothesis.strategies as st
import pytest

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_sum(num1, num2):    
    assert sum(num1, num2) == sum(num2, num1)
```

# Exercise 2

*Adapted from this [blog post](https://medium.com/russell-duhon/property-based-testing-from-scratch-in-python-bb1a8b56daf6).*

Say that we want to write a function to check whether someone is older than 21.
We'll start with the following code:
```python
import datetime

def check_age(birthday, today):
    return twenty_first(birthday) <= today

def twenty_first(birthday):
    return birthday + datetime.timedelta(days=365 * 21)
```

This seems to work for a few examples:
```python
birthday = datetime.date(1990, 5, 15)
today = datetime.date(2017, 1, 1)
assert check_age(birthday, today)

birthday = datetime.date(1990, 5, 15)
today = datetime.date(2000, 1, 1)
assert not check_age(birthday, today)
```

But it's not quite right (hint: leap years). 
One way we can test our code is by checking that for every birthday b, twenty_first(b) returns a date with the same month as b.
```python
import datetime
from hypothesis import given
from hypothesis.strategies import dates

def twenty_first(birthday):
    return birthday + datetime.timedelta(days=365 * 21)

@given(dates())
def test_must_be_in_same_month(birthday):
    error_message = """{} doesn't have the right twentyfirst birthday!
        Instead it has {}""".format(birthday, twenty_first(birthday))
    assert birthday.month == twenty_first(birthday).month, error_message
```

You should get an error that looks something like the following:
```
...
```

Let's try again.
```python
import datetime
import calendar

def twenty_first(birthday):
    # compute the number of leap years up to birthday
    leapdays = calendar.leapdays(birthday.year, birthday.year + 22)  # [first, second)
    if calendar.isleap(birthday.year) and birthday.month > 2:
        leapdays -= 1
    elif calendar.isleap(birthday.year + 1) and birthday.month < 3:
        leapdays -= 1
    # include this value when computing the result
    return birthday + datetime.timedelta(days=365 * 21 + leapdays)
```

This is almost right, but there is another tricky edge case (when is the 21st birthday of someone born on Feb. 29th?).
This code is copied in ex2.py. 
Use Hypothesis to find the bug, then fix the bug in the code (or the bug in the test) and verify that your test succeeds.

# Exercise 3

ex3.py contains some functions over lists. 
Use Hypothesis to find the bugs, and then fix them.

