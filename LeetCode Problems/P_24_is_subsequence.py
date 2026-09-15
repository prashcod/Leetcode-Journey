# IS SUBSEQUENCE : 
import re 

def is_subsequence(s , t): 
   pattern = ".*".join(list(s))
   match = re.search(pattern , t)
   if match : 
     return True 
   return False 
   

s = "abc"
t = "ahbgdc"
ans = is_subsequence(s ,t )
print(ans)