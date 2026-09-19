class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = str(bin(n))
        count = 0
        for char in bin_n:
            if char == "1":
                count+=1
        
        return count
