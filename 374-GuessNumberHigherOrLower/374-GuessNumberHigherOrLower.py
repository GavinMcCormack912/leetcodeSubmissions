# Last updated: 8/12/2025, 9:05:13 PM
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            m = (low+high) // 2
            if guess(m) == 1:
                low = m + 1
            elif guess(m) == -1:
                high = m
            else:
                return m
        
        # for if the range of answers is only 1
        return n