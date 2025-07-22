# Last updated: 7/21/2025, 8:35:30 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left+right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else: #  nums[middle] > target
                right = middle - 1
        return -1