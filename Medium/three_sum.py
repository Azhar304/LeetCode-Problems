# O(n**3) solution
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        combinations = []

        if n == 0:
            return "Empty list"

        for i in range(n):  
            for j in range(i+1, n): 
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        combinations.append([nums[i], nums[j], nums[k]])

        
        unique = set(tuple(sorted(x)) for x in combinations)
        return [list(x) for x in unique]

#two pointer solution 
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combinations = []
        n = len(nums)

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1

            while left < right :
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    combinations.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                elif total < 0 :
                    left+=1
                else:
                    right-=1

        return combinations
    
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))
