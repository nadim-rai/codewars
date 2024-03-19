'''
The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''

def count(s):
    # The function code should be here
    if len(s) == 0:
        return {}
    
    ans = {}
    
    sort_s = []
    [sort_s.append(x) for x in s if x not in sort_s] 
    
    for i in sort_s:
        if i in s:
            ans[i] = s.count(i)
    
    return ans

print(count('aba'))     #{'a': 2, 'b': 1}