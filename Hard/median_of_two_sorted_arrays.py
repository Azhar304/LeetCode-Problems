from typing import List
from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        
        if n % 2 == 1:  # odd length
            return merged[n // 2]
        else:           # even length
            return (merged[n//2 - 1] + merged[n//2]) / 2

        #OR just use median function

        # num = median(sorted(nums1 + nums2))
        # return num

nums1 = [1,3,5]
nums2= [2,4,6]
print(Solution().findMedianSortedArrays(nums1, nums2))