''' Reverse a list.
    E.g. reverse([1,2,3]) = [3,2,1]

    Example property:
    - reverse(reverse(l)) is equal to l
'''
def reverse(l):
    if len(l) > 0:
        return l[::-1]

''' Remove every occurrence of an element from a list.
    E.g. remove(2,[1,2,3]) = [1,3]

    Example property: 
    - the result of remove(x, l) does not contain x
'''
def remove(x, l):
    if len(l) == 0:
        return []
    for i in range(len(l)):
        if l[i] == x:
            return l[:i] + l[(i+1):]

''' Insert an item into a sorted list.
    E.g. insert(0,[1,2,3]) = [0,1,2,3]

    Example properties:
    - the result of insert(x, l) contains all the elements originally in l
    - if l is sorted, then insert(x, l) is sorted
'''
def insert(x, l):
    new_l = []
    for i in range(len(l)):
        if l[i] < x:
            new_l.append(l[i])
        else:
            return [x] + l[i:] 
    return [x] + new_l
      
''' Remove adjacent duplicates from a list.
    E.g. dedup([1,1,2,1,3,3]) = [1,2,1,3]

    Example property:
    - dedup(l) is the same as dedup(dedup(l))
'''
def dedup(l):
    i = 0
    new_l = []
    for i in range(0, len(l), 2):
        if l[i] == l[i+1]:
            new_l.append(l[i])
        else:
            new_l.append(l[i])
            new_l.append(l[i+1])
    return new_l
    
    
    
from hypothesis import given
import hypothesis.strategies as st

@given(st.lists(st.integers()))
def test_foo(l):
    assert (dedup(l) == dedup(dedup(l)))
            
