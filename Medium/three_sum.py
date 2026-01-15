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

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))