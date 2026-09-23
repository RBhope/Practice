class Solution:
    def reverseBits(self, n: int) -> int:
        num = f"{n:032b}"
        
        reversed_str = num[::-1]
        
        return int(reversed_str, 2)
