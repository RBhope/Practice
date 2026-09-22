class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0] * (n + 1)
        for i in range(n + 1):
            bin_n = str(bin(i))
            for char in bin_n:
                if char == "1":
                    count[i] += 1
        
        return count
