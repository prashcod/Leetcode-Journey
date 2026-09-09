# 3871. Count Commas in Range II : 
def countCommas (n): 
  str_val = str(n)
  if len(str_val) < 4 : 
    return 0 
  else : 
    no_seq = range(1000 , n+1 )
    count = len(no_seq)
  return count
    


n = 1004590
ans = countCommas(n)
print(ans)