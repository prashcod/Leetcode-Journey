# 167. Two Sum II - Input Array Is Sorted

#BRUTE FORCE : 
# def two_sum_ii(numbers , target): 
 
#   for i in range(len(numbers)):
#     j = i+1 
#     for j in range(len(numbers)):
#        if (numbers[i]+numbers[j]== target): 
#          return i , j
#   return 1 
    

# # numbers = [2,7,11,15] 
# numbers = [2,3,4]
# target = 9
# ans = two_sum_ii(numbers , target)
# print(ans)





def two_sum_ii(numbers , target): 
  i = 0 
  j = len(numbers)-1
  while i<j : 
    if (numbers[i] + numbers[j] == target) : 
      return i+1 , j+1 
    elif (numbers[i]+numbers[j]>target): 
      j -= 1 
    else : 
      i += 1 
  return 0 
  

numbers = [2,7,11,15] 
# numbers = [2,3,4]
target = 9
ans = two_sum_ii(numbers , target)
print(ans)

# MY SOLUTION : 
# Solved 167 : Two Sum II - Input Array Is Sorted

# Prashant Gyawali
# Jan LeetCoding Challenge
# 0
# a few seconds ago
# Python3
# Intuition
# First I tried out the Brute force apporach where I used o(n^2)
# time complexitity then later I used two pointers convergining pointers apporach

# Approach
# Used Two pointers Converging pointers and IF-ELSE condition

# Complexity
# Time complexity:
# O(n)

# Space complexity:
# O(1)