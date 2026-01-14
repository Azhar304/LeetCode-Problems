class Solution:
    def reverse(self, x: int) -> int:
        rev_x = 0
        abs_x = abs(x) # makes x positive integer if negatuve
        sign = -1 if x<0 else 1

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while abs_x>0:

            r = abs_x % 10 #3 #2 #1
            abs_x = abs_x // 10 #12 #1 #0
            
            if rev_x > (INT_MAX - r) // 10:
                return 0

            rev_x = rev_x*10 + r  #0*10+3=3 , 3*10+2=32,  32*10+1 =321

            
        return rev_x*sign        
x=-123456789
print(Solution().reverse(x))