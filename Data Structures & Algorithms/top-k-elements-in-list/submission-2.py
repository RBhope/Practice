class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter()
        for val in nums:
        
            if val in count:
                count[val] = 1 + count[val]
            else:
                count[val] = 1
        
        return [item for item,freq in count.most_common(k)]


