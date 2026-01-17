#solution using math
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        
        sqrt = math.sqrt(x)
        sqrt = math.floor(sqrt) 
        return sqrt
    
#brute force solution
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        i = 2
        while i * i <= x:
            i += 1
        
        return i - 1
        
x = 8
print(Solution().mySqrt(x))