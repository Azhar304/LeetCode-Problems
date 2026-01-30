class Solution:
    def myPow(self, x: float, n: int) -> float:
        #suppose for x=3, n =5
        ans = 1 #we assume initial answer to be 1 : ans 3 : ans still 3
        power = abs(n) # makes n positive : power = 2 : power =1

        while(power>0): # 1 : 5>0(true) : 2 > 0 (true) : 1 > 0 : loop stops
            if power%2==1: # 5%2==1(true) : 2%2==0(False) : 1 % 2 ==1 (true)
                ans*=x # ans = 1 * 3 = 3 : skip : ans = 3* 81

            x*=x # 3*3 =9 : 9 * 9 =81 : 81*81
            power//=2 # 5 // 2 = 2 : 2//2 =1 , 1//2 = 0
        return ans if n>0 else 1/ans #return 3*81
    
print(Solution().myPow(3.0,5))