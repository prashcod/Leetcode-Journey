#Power of Three 

def PowerOfThree(n): 
   if (n <= 0) : 
     return False 
   if (n == 1 ): 
     return True 
   if ( n % 3 != 0) : 
     return False 
   return PowerOfThree(n/3)
  



n = 27 
ans = PowerOfThree(n)
print(ans)