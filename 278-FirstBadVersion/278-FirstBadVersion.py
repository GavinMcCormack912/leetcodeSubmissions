# Last updated: 8/12/2025, 9:05:15 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n-1

        while l < r:
            m = (l+r)//2

            if isBadVersion(m+1):
                if not isBadVersion(m):
                    return m+1
                else:
                    r = m
            else:
                l = m + 1

        # for if it's an array of size 1
        return n