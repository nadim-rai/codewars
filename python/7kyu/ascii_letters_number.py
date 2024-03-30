'''
You have to create a function that converts integer given as string into ASCII uppercase letters or spaces.

All ASCII characters have their numerical order in table.

For example,

from ASCII table, character of number 65 is "A".
Numbers will be next to each other, So you have to split given number to two digit long integers.

Examples (input -> output)
'658776' -> 'AWL' (because in ASCII table 'A' is 65, 'W' is 87, 'L' is 76)
'73327673756932858080698267658369' ->'I LIKE UPPERCASE'

import codewars_test as test
from solution import convert

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(convert("65"),"A")
        test.assert_equals(convert("656667"),"ABC")
        test.assert_equals(convert("676584"),"CAT")
        test.assert_equals(convert("73327673756932858080698267658369"),"I LIKE UPPERCASE")
'''

def convert(number):
    arr = []
    for i in range(0, len(number), 2):
        arr.append(int(number[i:i+2]))
    return ''.join(chr(num) for num in arr)

print(convert('73327673756932858080698267658369'))      #I LIKE UPPERCASE