#Recursive Binary Search 

def recursiveBinarySearch(arr , target ,st , en):
    
    if st <= en : 
      mid = st + (en-st) // 2
      if target == arr[mid]: 
        return mid 
      if target <= arr[mid] : 
        return recursiveBinarySearch(arr ,target , st , mid-1 )
      elif target >=  arr[mid] : 
        return recursiveBinarySearch (arr , target , mid+1 , en)
    return -1   



arr = [-1, 0 , 3 , 5, 9 ,12 ]
target = 9 
st = 0 
en = len(arr)-1 
ans =recursiveBinarySearch(arr , target ,st , en)
print(ans) 
  