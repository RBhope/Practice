class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        # Loop exactly 32 times for a 32-bit integer
        for _ in range(32):
            # 1. Shift your result left to make room for the incoming bit
            res <<= 1
            
            # 2. Extract the rightmost bit of n and add it to res
            res |= (n & 1)
            
            # 3. Shift n right to discard the bit we just processed
            n >>= 1
            
        return res
