'''
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false

'''
def is_square(n):  
    num = len(str(n**0.5).split(".")[1])
    if num > 1:
        return False
    return True 

print(is_square(2))        #True