class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0,len(nums)):
            c = target - nums[i]
            if c in nums:
                c_index = nums.index(c)
                if (i!=c_index):
                    return [min(i,c_index), max(i,c_index)]