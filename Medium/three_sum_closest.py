from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]  

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # update closest sum if this is closer to target
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                # move pointers
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # exact match
                    return total

        return closest_sum

nums = [-1, 0, 1, 2, -1, -4]
target = 4
print(Solution().threeSumClosest(nums, target))
