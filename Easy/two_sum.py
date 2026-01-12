# class Solution:
#     def two_sum(self, nums, target):
#         result = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 s = nums[i] + nums[j]
#                 if s == target:
#                     result.append(i)
#                     result.append(j)
#         return result

# nums= [2,7,11,15]
# target=9

# print(Solution().two_sum(nums,target))


#HashMap
class Solution:
    def twoSum(self , nums:list[int], target:int):
        num_map={}
        n= len(nums)

        for i in range(n):
            num_map[nums[i]] = i

        for i in range (n):
            complement = target - nums[i]
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]
            
        return []

nums = [2, 7, 11, 15]
target = 18
print(Solution().twoSum(nums,target)) #[1,2] in this case

           

