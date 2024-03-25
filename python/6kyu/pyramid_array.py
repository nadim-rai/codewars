'''
Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]

Note: the subarrays should be filled with 1s

import codewars_test as test
from solution import pyramid

@test.describe("Pyramid Array")
def pyramid_tests():
    @test.it("Sample Tests")
    def sample_tests():
        test.assert_equals(pyramid(0), [])
        test.assert_equals(pyramid(1), [[1]])
        test.assert_equals(pyramid(2), [[1], [1, 1]])
        test.assert_equals(pyramid(3), [[1], [1, 1], [1, 1, 1]])
'''

def pyramid(n):
    ans = []
    for i in range(1, n+1, 1):
        ans.append([1] * i)
    return ans

print(pyramid(4))           #[[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]