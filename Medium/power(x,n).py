class Solution:
    def myPow(self, x: float, n: int) -> float:
        #suppose for x=3, n =5
        ans = 1 #we assume initial answer to be 1 : ans 3 , 
        power = abs(n) # makes n positive : power = 2

        while(power>0): # 1 : 5>0(true) : 2 > 0 (true)
            if power%2==1: # 5%2==1(true) : 2%2==0
                ans*=x # ans = 1 * 3 = 3 : skip

            x*=x # 3*3 =9 : 9 * 9 =81
            power//=2 # 5 // 2 = 2 : 2//2 =1
        return ans if n>0 else 1/ans
    
print(Solution().myPow(3.0,5))