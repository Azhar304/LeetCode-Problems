# Cpp solution
# class Solution {
# public:
#     int maxSubArray(vector<int>& nums) {
#         int currSum=0 , maxSum = INT_MIN ;
#         for(int val : nums){
#             currSum += val;
#             maxSum = max(currSum, maxSum);

#             if (currSum<0 ){
#                 currSum =0 ;
#             }
#         }
#         return maxSum ;

        
#     }
# };

#python implementation
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = float('-inf')
        for val in nums:
            currSum+=val
            maxSum= max(currSum, maxSum)

            if currSum < 0:
                currSum = 0

        return maxSum