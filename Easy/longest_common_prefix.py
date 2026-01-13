class Solution:
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix= ""
        for i in range(len(strs[0])):  
            char = strs[0][i]           
            match = True

            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    match = False
                    break

            if not match:
                break
            prefix += char

        return prefix
        

strs = ["blow", "bow", "ball"]    
print(Solution().longestCommonPrefix(strs))