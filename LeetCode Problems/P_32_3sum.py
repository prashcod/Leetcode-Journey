#3 sum problem : 

#BRUTE FORCE : 

# def three_sum(nums): 
#   res = set()
#   for i in range(len(nums)): 
#     for j in range(i , len(nums)): 
#        for k in range(j ,len(nums)): 
#              if (nums[i]+ nums[j] + nums[k] != 0): 
#                continue 
#              elif(i!=j and i!=k and j!=k and [nums[i],nums[j],nums[k]]!= [nums[j],nums[i],nums[k]and [nums[i],nums[k],nums[j] != nums[k],nums[j],nums[i]] ]): 
#                res.add([nums[i] , nums[j] , nums[k]])
#   return list(res)


#brute force another apporach : 
# def three_sum(nums):
#     res = set()
    
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):      # Starts AFTER i
#             for k in range(j + 1, len(nums)):  # Starts AFTER j
                
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     # Automatically removes duplicate sequences by sorting into a tuple
#                     res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    
#     return [list(t) for t in res]
# nums = [-1,0,1,2,-1,-4]
# ans = three_sum(nums)
# print(ans)

#optimized apporach : 
def three_sum(nums): 
  nums.sort()
  res = []
  i = 0 
  j= i+1 
  k = len(nums)-1 
  while i<j<k :
    if (nums[i] + nums[j] + nums[k] == 0 and i!=j and j!=k and i!=k): 
      res.append([nums[i] , nums[j] , nums[k]]) 
    elif (nums[i] + nums[j] + nums[k] < 0 and j<k): 
       j += 1 
       continue 
    elif (nums[i] + nums[j] + nums[k] > 0 and k>j) : 
       k -= 1 
       continue 
    return res 
  

nums = [-1,0,1,2,-1,-4]
ans = three_sum(nums)
print(ans)

