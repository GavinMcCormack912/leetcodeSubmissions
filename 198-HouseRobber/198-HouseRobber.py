# Last updated: 8/27/2025, 3:52:27 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1-D Dynamic Programming
        # You can't get adjacent houses, so you'll need to compare values using 
        # newVal = arr[n] + max(arr[n-2], arr[n-3])
        num_houses = len(nums)
        if num_houses == 1:
            return nums[0]
        if num_houses == 2:
            return max(nums[0], nums[1])
        money = [0] * num_houses
        max_money = 0
        # first 3 values done
        money[0] = nums[0]
        money[1] = nums[1]
        money[2] = nums[0] + nums[2]
        # check for max money value before looping through rest of houses
        max_money = max(money[2], money[1])
        # Use repeating max house robbery value paths to build on the current house value
        # If it's higher than the max robbery value, change the max val
        i = 3
        while i < num_houses:
            money[i] = nums[i] + max(money[i-2], money[i-3])
            if money[i] > max_money:
                max_money = money[i]
            i += 1
        return max_money

