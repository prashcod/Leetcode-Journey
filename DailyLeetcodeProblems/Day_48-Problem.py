# 3870. Count Commas in Range
def counting_commas(n): 
  str_val=str(n)
  if (len(str_val)!= 4): 
    return 0
  else : 
    no_seq = range(1000, n+1)
    count = len(no_seq)
  return count 

n = 1002
ans=counting_commas(n)
print(ans)