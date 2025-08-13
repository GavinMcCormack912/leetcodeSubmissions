# Last updated: 8/12/2025, 9:05:29 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []
        subset = []
        if not nums:
            return powerset
        n = len(nums)
        
        def dfs(start_idx):
            nonlocal powerset
            nonlocal nums
            nonlocal subset
            nonlocal n

            #check for end
            if start_idx >= n:
                powerset.append(subset.copy())
                return
            
            subset.append(nums[start_idx])
            dfs(start_idx + 1)

            subset.pop()
            dfs(start_idx + 1)

        start = 0
        dfs(start)
        return powerset