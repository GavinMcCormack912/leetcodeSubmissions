# Last updated: 10/1/2025, 5:59:45 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * (len(nums) + 1)
        right = [1] * (len(nums) + 1)

        for i in range(1, len(left)):
            left[i] *= left[i-1] * nums[i-1]
        
        for j in range(len(right) - 2, -1, -1):
            right[j] = right[j+1] * nums[j]

        res = []
        for i in range(len(nums)):
            res.append(right[i+1] * left[i])
        
        return res
