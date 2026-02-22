class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1      # position of previous 1 bit
        max_gap = 0
        position = 0   # current bit position
        
        while n > 0:
            if n & 1:  # last bit is 1
                if prev != -1:
                    max_gap = max(max_gap, position - prev)
                prev = position
            n = n >> 1
            position += 1
            
        return max_gap

