from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        current_sum = 0
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            
            maxSum = max(maxSum, current_sum)
            
        return maxSum
