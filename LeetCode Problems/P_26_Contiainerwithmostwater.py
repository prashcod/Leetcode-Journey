# 11. Container With Most Water
#most asked question : 
def most_water(heignt): 
  lp = 0 
  rp = len(heignt)-1 
  max_area = 0 
  while (lp < rp): 
    wi = (rp - lp)
    ht = min(height[lp] , heignt[rp])
    area = wi * ht 
    max_area = max(max_area , area)
    if height[lp]<height[rp]: 
      lp += 1 
    else : 
      rp -= 1
  return max_area
  


height = [1,8,6,2,5,4,8,3,7]
ans = most_water(height)
print(ans)