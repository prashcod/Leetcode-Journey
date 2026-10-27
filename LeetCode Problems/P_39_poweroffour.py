#POWER OF FOUR : 

def isPowerOfFour( n) : 
        if n <= 0 : 
            return False 
        if n == 1 : 
            return True 
        if n % 4 != 0 : 
            return False 
        return isPowerOfFour(n/4)

n = 16  
ans = isPowerOfFour(n)
print(ans)