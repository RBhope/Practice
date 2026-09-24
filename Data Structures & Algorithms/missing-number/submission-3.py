class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in range(len(nums)+1):
            if i not in nums:
                missing = i
        return missing
