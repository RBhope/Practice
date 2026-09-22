class Solution:
    def countBits(self, n: int) -> List[int]:
        count=[0]*(n+1)
        for i in range(n+1):
            count[i] = i.bit_count()
        return count