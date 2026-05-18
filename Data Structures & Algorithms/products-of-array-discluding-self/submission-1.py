class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        prod=1
        res = [1]*len(nums)
        for i in nums:
            if i==0:
                zeroCount+=1
            else:
                prod = prod*i
        
        for i in range(len(nums)):
            if zeroCount>1:
                res[i]=0
            elif zeroCount==1:
                res[i] = prod if nums[i] == 0 else 0
            else:
                res[i]= int(prod//nums[i])
        return res
