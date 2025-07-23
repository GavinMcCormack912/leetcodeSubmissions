# Last updated: 7/23/2025, 7:03:13 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set and two index keys
        # reset the set and move the left index key to the spot of
        # the right key when a duplicate char is found

        left = 0
        right = 0
        max_str = 0
        char_dict = {}
        while right < len(s):
            if s[right] in char_dict.keys():
                if left < char_dict[s[right]] + 1:
                    left = char_dict[s[right]] + 1 # move up left ptr to idx after last repeat letter occurence
                char_dict[s[right]] = right #update to current idx
            else:
                char_dict[s[right]] = right
            # always make right index go up
            str_len = right - left + 1
            max_str = max(max_str, str_len)
            right += 1
        
        return max_str
