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
    

