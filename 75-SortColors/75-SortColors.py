# Last updated: 8/12/2025, 9:05:30 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorCount = {}
        if not nums:
            return
        maxNum = nums[0]
        for num in nums:
            colorCount[num] = colorCount.get(num, 0) + 1
            if num > maxNum:
                maxNum = num
        
        # go through each bucket. re-add them color by color, by how many exist
        idx = 0
        color = 0
        if not colorCount:
            return
        while color < maxNum + 1:
            for _ in range(colorCount.get(color,0)): #number of elements per color
                nums[idx] = color
                idx += 1
            color += 1