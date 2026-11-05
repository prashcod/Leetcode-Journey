# 1385. Find the Distance Value Between Two Arrays
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

# Example 1:

# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation: 
# For arr1[0]=4 we have: 
# |4-10|=6 > d=2 
# |4-9|=5 > d=2 
# |4-1|=3 > d=2 
# |4-8|=4 > d=2 
# For arr1[1]=5 we have: 
# |5-10|=5 > d=2 
# |5-9|=4 > d=2 
# |5-1|=4 > d=2 
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2

from bisect import bisect_left

def findTheDistanceValue(arr1 , arr2 , d) : 
        arr2.sort()

        count = 0

        for x in arr1:
            idx = bisect_left(arr2, x)

            left_ok = (idx == 0 or x - arr2[idx - 1] > d)

            right_ok = (idx == len(arr2) or arr2[idx] - x > d)

            if left_ok and right_ok:
                count += 1

        return count
  
  

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
ans = findTheDistanceValue(arr1 , arr2 , d)
print(ans)