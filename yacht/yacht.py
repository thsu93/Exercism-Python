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
    count = len(set(dice))
    s = sorted(dice)
    if category < 7:
        return sum([i for i in dice if i==category])
    if category == 7:
        if count == 2 and s[0]==s[1] and s[3]==s[4]:
            if s[2] == s[0]:
                return s[0]*3 + s[4]*2
            else:
                return s[0]*2 + s[4]*3
        return 0
    if category==8:
        if count <= 2:
            if s[0]==s[1] and s[0]==s[3]:
                return 4*s[0]
            elif s[1]==s[4]:
                return 4*s[1]
            else:
                return 0
        return 0
    if category==9:
        if s == [1,2,3,4,5]:
            return 30
        return 0
    if category==10:
        if s == [2,3,4,5,6]:
            return 30
        return 0
    if category==11:
        return sum([i for i in dice])
    if category==12:
        if count == 1:
            return 50
        return 0
        
