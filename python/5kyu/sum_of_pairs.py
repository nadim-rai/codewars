'''
Sum of Pairs
Given a list of integers and a single sum value, return the first two values (parse from the left please)
in order of appearance that add up to form the sum.

If there are two or more pairs with the required sum, the pair whose second element has the smallest
index is the solution.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * the correct answer is the pair whose second value has the smallest index
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * the correct answer is the pair whose second value has the smallest index
== [3, 7]
Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code 
doesn't time out.
'''

def sum_pairs(ints, s):
    ans_set = set()
    for n in ints:
        if s-n in ans_set:
            return[s-n ,n]
        ans_set.add(n)

print(sum_pairs([1, -2, 3, 0, -6, 1],-6))       #[0, -6]
# def sum_pairs(ints, s):
#   ans = []
#   index_list= []
#   for i in range(len(ints)):
#     for j in range(i+1, len(ints)):
#       if ints[i] + ints[j] == s:
#         ans.append([ints[i], ints[j]])
#         index_list.append(j)
#   if len(index_list) !=0:
#     min_value = min(index_list)
#     min_index = index_list.index(min_value)
#     return ans[min_index]
#   else:
#     return None