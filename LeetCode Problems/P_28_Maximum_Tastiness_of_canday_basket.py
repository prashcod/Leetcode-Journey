class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n=len(price)
        price.sort()
        
        def check(x):
            count=1
            prev=price[0]

            for i in range(1,n):
                if  price[i]-prev>=x:
                    count+=1
                    prev=price[i]
            return count>=k

        
        low=0
        high=max(price)-min(price)
        ans=-1
        
        while low<=high:
            mid=(low+high)//2
            if check(mid)==True:
                low=mid+1
                ans=mid
            else:
                high=mid-1
        
        return ans