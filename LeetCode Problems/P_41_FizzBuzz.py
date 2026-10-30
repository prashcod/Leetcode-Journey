#FIZZ BUZZ 

def fizzbuzz(n): 
    res = []
    for i in range(1,n+1): 
        i = str(i)
        res.append(i)
    for idx in range( len(res)) : 
       if int(res[idx]) % 3 == 0 and int(res[idx]) % 5 == 0: 
          res[idx] = 'FizzBuzz'
       elif int(res[idx]) %3 == 0 : 
          res[idx ] = 'Fizz'
       elif int(res[idx]) %5 == 0 : 
          res[idx] = 'Buzz'
    return res



n = 3
ans = fizzbuzz(n)
print(ans)