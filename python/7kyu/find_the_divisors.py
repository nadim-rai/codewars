'''Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with 
all of the integer's divisors(except for 1 and the number itself), from smallest to largest. 
If the number is prime return the string '(integer) is prime' 
(null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust). 

Example
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

import codewars_test as test
from solution import divisors

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(divisors(15), [3,5], "integer = 15")
        test.assert_equals(divisors(253), [11,23], "integer = 253")
        test.assert_equals(divisors(24), [2,3,4,6,8,12], "integer = 24")
        test.assert_equals(divisors(25), [5], "integer = 25")
        test.assert_equals(divisors(13), "13 is prime", "integer = 13")
        test.assert_equals(divisors(3), "3 is prime", "integer = 3")
        test.assert_equals(divisors(29), "29 is prime", "integer = 29")

'''


def divisors(integer):
    arr = []
    for i in range(2, integer):
        if integer % i == 0:
            arr.append(i)
    res = arr if arr else f"{integer} is prime"
    return res

print(divisors(25)) #5

'''
Other solutions from Codewars

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

def divisors(integer):
  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)

divisors = lambda z: [i for i in range(2,z) if z % i == 0] or ("%d is prime" % z)

'''