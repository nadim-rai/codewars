'''
Given a string s, your task is to return another string such that even-indexed and 
odd-indexed characters of s are grouped and the groups are space-separated. Even-indexed group 
comes as first, followed by a space, and then by the odd-indexed part.

Examples
input:    "CodeWars" => "CdWr oeas"
           ||||||||      |||| ||||
indices:   01234567      0246 1357
Even indices 0, 2, 4, 6, so we have "CdWr" as the first group.
Odd indices are 1, 3, 5, 7, so the second group is "oeas".
And the final string to return is "Cdwr oeas".

Notes
Tested strings are at least 8 characters long.

STRINGS FUNDAMENTALS SORTING
'''

def sort_my_string(s):
    even = []
    odd = []
    for i in range(len(s)):
        if i%2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    return ''.join(even) + ' ' + ''.join(odd)

print(sort_my_string("CodeWars"))       #CdWr oeas"

# Solved by SimonSlominski, Sergey Kazantsev, kazus, im_aj, StephenDonovan1, YerbolatD, Azearia, xq1542, Sigmanificient, mohamed abdullah hamed, oibioib (+ 69)
# def sort_my_string(s):
#     return f'{s[::2]} {s[1::2]}'
