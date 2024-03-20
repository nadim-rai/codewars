'''
an array where an uppercase letter is a person standing up. 

Rules
1.  The input string will always be lower case but maybe empty.

2.  If the character in the string is whitespace then pass over it as if it was an empty seat

wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
'''

def wave(people):
    # Code here
    ans = []
    for i in range(len(people)):
        if people[i] == ' ':
            continue
        else:
            ans.append(people[:i] + people[i].upper() + people[i+1:])
    
    return ans

print(wave(" gap "))      #[' Gap ', ' gAp ', ' gaP ']