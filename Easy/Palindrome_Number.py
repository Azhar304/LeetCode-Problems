"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_num = 0
        original_num = x

        if x < 0 :
            return False
        
        while(x > 0):
            
            digit = x % 10
            rev_num = rev_num*10 + digit
            x= x//10

        if rev_num == original_num:
            return True
        return False
    
x = 1234
print(Solution().isPalindrome(x))

