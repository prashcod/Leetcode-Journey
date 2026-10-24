#Fibonacci sereries using recursion 

class Solution : 
  def fib(self, n: int) -> int:
        #base case 
        if n ==1 : 
            return 1
        elif n == 0 : 
            return 0
        return self.fib(n-1)+ self.fib(n-2)
     
n =2
obj = Solution()
print(obj.fib(n))

