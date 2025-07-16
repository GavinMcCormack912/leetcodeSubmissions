# Last updated: 7/16/2025, 7:29:34 PM
class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        return len(nums_set) < len(nums)
        