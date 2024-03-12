'''
In this kata you will create a function that takes a list of non-negative integers and strings 
and returns a new list with the strings filtered out.
'''

def filter_list(l):
    'return a new list with the strings filtered out'
    return [num for num in l if type(num) == int]

print(filter_list([1,2,'aasf','1','123',123]))  #returns [1,2,123]
