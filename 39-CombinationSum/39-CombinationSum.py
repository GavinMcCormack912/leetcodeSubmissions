# Last updated: 8/12/2025, 9:05:33 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        targetPaths = []
        if not candidates:
            return targetPaths
        n = len(candidates)
        curr_path = []

        def dfs(idx, total):
            nonlocal target
            nonlocal n
            nonlocal candidates
            nonlocal curr_path
            # Base Case Checks
             # do we have a target value? append the path if so
            if total == target:
                targetPaths.append(curr_path.copy())
                return
                
            if idx >= n:
                return
            if total > target:
                return

            # use curr value
            curr_path.append(candidates[idx])
            new_total = total + candidates[idx]
            dfs(idx, new_total)

            #go to new value
            curr_path.pop()
            dfs(idx+1, total)
            

        dfs(0, 0)
        return list(targetPaths)