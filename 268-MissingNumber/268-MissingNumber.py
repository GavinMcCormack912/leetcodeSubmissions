# Last updated: 9/23/2025, 11:09:47 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = len(nums)
        remainingSum = maxNum * (maxNum + 1) / 2
        for i in range(len(nums)):
            remainingSum -= nums[i]
        return int(remainingSum)