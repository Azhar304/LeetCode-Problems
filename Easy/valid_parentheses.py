
class Solution:
    def isValid(self, s:str)->bool:

        if len(s)%2 != 0:
            return False
        
        stack= []
        pairs = {')':'(', 
                 '}':'{',
                 ']':'['}
        
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack.pop()!= pairs[ch]:
                    return False

        return len(stack)==0
s ='([{}])'

print(Solution().isValid(s))