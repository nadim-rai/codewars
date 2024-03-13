'''
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
'''

def get_count(sentence):
    count = 0
    for i in range(len(sentence)):
        if sentence[i] == 'a' or sentence[i] == 'e' or sentence[i] == 'i' or sentence[i] == 'o' or sentence[i] == 'u':
            count +=1
    return count

print(get_count("I love apples"))