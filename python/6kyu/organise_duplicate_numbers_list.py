'''
Sam is an avid collector of numbers. Every time he finds a new number he throws it on the 
top of his number-pile. Help Sam organise his collection so he can take it to 
the International Number Collectors Conference in Cologne.

Given an array of numbers, your function should return an array of arrays, where each subarray 
contains all the duplicates of a particular number. Subarrays should be in the same order as 
the first occurence of the number they contain:

group([3, 2, 6, 2, 1, 3])
>>> [[3, 3], [2, 2], [6], [1]]
'''

def group(arr):
  ans = []
  remove_dup = set(arr)
  for i in arr:
    if i in remove_dup:
        remove_dup.remove(i)
        ans.append([i] * arr.count(i))
  return ans

print(group([3, 2, 6, 2, 1, 3]))      #[[3, 3], [2, 2], [6], [1]]

# def group(arr):
#     dubArray = []
#     while len(arr) > 0:
#         item = arr[0]
#         itemArr = [item]
#         arr = arr[1:]
#         i = 0
#         while i < len(arr):
#             if item == arr[i]:
#                 itemArr.append(arr[i])
#                 arr.pop(i)
#             else:
#                 i += 1
#         if len(itemArr) > 0:
#             dubArray.append(itemArr)
#     return dubArray