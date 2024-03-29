from hypothesis import given, example
from hypothesis.strategies import text

def encode(input_string):
    if not input_string:
        return []

    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            # oops! we forgot the following line
            # count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

@given(text())
@example("")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
