# Last updated: 8/1/2025, 10:27:21 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        water = 0


        lmax = height[0]
        rmax = height[-1]

        # get max on the left for any height idx
        for i in range(len(height)):
            if height[i] > lmax:
                lmax = height[i]
            leftMax[i] =  lmax

        # get max on the right for any height idx
        for i in range(len(height)-1, -1, -1):
            if height[i] > rmax:
                rmax = height[i]
            rightMax[i] =  rmax

        for i in range(len(height)):
            water_level = min(leftMax[i], rightMax[i])
            water += water_level - height[i]
    

        return water
        