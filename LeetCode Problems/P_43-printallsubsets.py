# Using REcursion concept we print all subsets : 
  
  
def printallsubsets( arr,ans , i , res):
    if i == len(arr):
        res.append(ans[::-1])
        return 
    
    ans.append(arr[i])
    printallsubsets(arr, ans, i + 1, res)
    ans.pop()
    printallsubsets(arr, ans, i + 1, res)
  

def subset(arr): 
    ans = []
    res = []
    i = 0 
    arr = arr[::-1]
    printallsubsets(arr,ans,i ,res)
    res.reverse()
    return res

arr = [1,2,3]
ansp =subset(arr)
print(ansp)