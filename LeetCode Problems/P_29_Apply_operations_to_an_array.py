def applyoperations(nums): 
  i = 0 
  j = i+ 1 
  while i <= j and j< len(nums):
    if nums[i] == nums[j]: 
      nums[i] *= 2 
      nums[j] = 0 
    else : 
      i += 1 
      j += 1 
      continue 
    i += 1 
    j += 1 
  
  left = 0 
  for right in range(len(nums)): 
    if nums[right] != 0: 
      nums[left], nums[right] = nums[right], nums[left]
      left += 1 
    
  return nums 


nums = [ 1, 2 ,2 , 1, 1 , 0]
ans = applyoperations(nums)
print(ans)