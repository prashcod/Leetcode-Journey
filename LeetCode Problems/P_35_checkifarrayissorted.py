#CHECK IF ARRAY IS SORTED OR NOT : 
def isSorted(arr,n): 
  if (n == 0 or n == 1 ): 
     return True 
  return arr[n-1] >= arr[n-2] and isSorted(arr , n-1)


arr = [1,2,3,4,8]

ans = isSorted(arr , 5)
print(ans)