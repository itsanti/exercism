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


# Score categories.
# Change the values as you see fit.
YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    result = 0
    if category < 7:
        result = dice.count(category) * category
    elif category == FULL_HOUSE:
        if len(set(dice)) == 2:
            pair = list(set(dice))
            if dice.count(pair[0]) == 2 or dice.count(pair[0]) == 3:
                result = sum(dice)
    elif category == FOUR_OF_A_KIND:
        if len(set(dice)) == 2:
            pair = list(set(dice))
            if dice.count(pair[0]) == 4:
                result = pair[0] * 4
            elif dice.count(pair[0]) == 1:
                result = sum(dice) - pair[0]
        elif len(set(dice)) == 1:
            result = dice[0] * 4
    elif category == LITTLE_STRAIGHT:
        if all(digit in dice for digit in range(1, 6)):
            result = 30
    elif category == BIG_STRAIGHT:
        if all(digit in dice for digit in range(2, 7)):
            result = 30
    elif category == CHOICE:
        result = sum(dice)
    elif category == YACHT:
        if sum(dice) == dice[0] * len(dice):
            result = 50
    return result
