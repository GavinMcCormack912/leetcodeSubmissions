# Last updated: 10/1/2025, 5:16:19 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for num in nums[1:]:
            curSum = max(curSum, 0) + num

            if curSum > maxSum:
                maxSum = curSum
        return maxSum
        