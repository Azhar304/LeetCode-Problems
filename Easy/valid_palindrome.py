"""Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 """


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        
        return cleaned == cleaned[::-1]
    

#two pointer solution

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s)-1
        while left < right:

        # moving left pointer
            while left < right and not s[left].isalnum():
                    left += 1

            # moving right pointer
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower()!= s[right].lower():
                return False
            
            left+=1
            right-=1

        return True