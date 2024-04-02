'''
You receive some random elements as a space-delimited string. Check if the elements are part of an 
ascending sequence of integers starting with 1, with an increment of 1 (e.g. 1, 2, 3, 4).

Return:

0 if the elements can form such a sequence, and no number is missing ("not broken", e.g. "1 2 4 3")
1 if there are any non-numeric elements in the input ("invalid", e.g. "1 2 a")
n if the elements are part of such a sequence, but some numbers are missing, and n is the lowest of them 
("broken", e.g. "1 2 4" or "1 5")

Examples
"1 2 3 4"  ==>  return 0, because the sequence is complete

"1 2 4 3"  ==>  return 0, because the sequence is complete (order doesn't matter)

"2 1 3 a"  ==>  return 1, because it contains a non numerical character

"1 3 2 5"  ==>  return 4, because 4 is missing from the sequence

"1 5"      ==>  return 2, because the sequence is missing 2, 3, 4 and 2 is the lowest

import codewars_test as test
from solution import find_missing_number

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_missing_number("1 2 3 5"),4,"It must work for missing middle terms")
        test.assert_equals(find_missing_number("1 5"),2,"It must work for missing more than one element")
        test.assert_equals(find_missing_number(""), 0,"It must return 0 for an empty sequence")
        test.assert_equals(find_missing_number("1 2 3 4 5"),0,"It must return 0 if no number is missing")
        test.assert_equals(find_missing_number("2 3 4 5"),1,"It must return 1 for a sequence missing the first element")
        test.assert_equals(find_missing_number("2 6 4 5 3"),1,"It must work for a shuffled input")
        test.assert_equals(find_missing_number("_______"),1,"It must return 1 for an invalid sequence")
        test.assert_equals(find_missing_number("2 1 4 3 a"),1,"It must return 1 for an invalid sequence")
        test.assert_equals(find_missing_number("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
        23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 
        55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 
        87 88 89 91 92 93 94 95 96 97 98 99 100 101 102"),90,"It must return 90")

'''

import re

def find_missing_number(sequence):
    if sequence == "":
        return 0
    elif len(sequence) == 1:
        return 1
    elif not re.match(r'^(\d+ )+\d+$', sequence):
        return 1
    else:
        arr = list(map(int, sequence.split(' ')))
        max_val = max(arr)
        for i in range(1, max_val):
            if i not in arr:
                return i
        return 0
    

print(find_missing_number("1 5"))           #2