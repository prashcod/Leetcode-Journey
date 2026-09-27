#SQUARES OF SORTED ARRAY : 

def sortedSquare( nums): 
  yoyo = list(map(lambda x : x**2 , nums))
  yoyo.sort()
  return yoyo

nums = [ -4 ,-1 ,0 , 3 ,10 ]
ans = sortedSquare(nums)
print(ans)