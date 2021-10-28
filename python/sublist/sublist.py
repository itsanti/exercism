"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    strone = ','.join(map(str, list_one))
    strtwo = ','.join(map(str, list_two))
    if strone in strtwo:
        if len(strone) != len(strtwo):
            return SUBLIST
        else:
            return EQUAL
    elif strtwo in strone and len(strone) != len(strtwo):
        return SUPERLIST
    else:
        return UNEQUAL
