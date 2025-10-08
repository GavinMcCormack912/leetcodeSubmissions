# Last updated: 10/7/2025, 11:36:43 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dict of already-used letters and their indices
        letters = {}

        left = 0
        right = 0
        res = 0
        n = len(s)

        # go through len of string with the "right" pointer as the limiter
        while right < n:
            #check if new element is in set, else add 1 to the substring length
            if s[right] in letters.keys():
                left = max(left, letters[s[right]] + 1)
            # check if youre at a new largest size
            res = max(res, right-left + 1)
            # mark down letter just seen
            letters[s[right]] = right
            right += 1

        return res