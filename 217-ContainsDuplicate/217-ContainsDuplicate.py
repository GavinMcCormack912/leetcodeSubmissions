# Last updated: 7/16/2025, 7:28:28 PM
class Solution(object):
    def containsDuplicate(self, nums):
        nums_dict = dict()
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        for val in nums_dict.values():
            if val >= 2:
                return True
        return False
        