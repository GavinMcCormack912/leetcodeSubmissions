# Last updated: 10/1/2025, 8:03:40 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # basically, two pointer sum with a for loop

        # first, sort the arrays. this is O(n) space
        sorted_nums = sorted(nums)
        print(sorted_nums)
        res = []
        for i in range(len(sorted_nums) - 2):
            n = sorted_nums[i]
            if n > 0:
                break
            
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            l = i + 1
            r = len(sorted_nums)-1
            print("Starting num:", n)
            while l < r:
                left_val = sorted_nums[l]
                right_val = sorted_nums[r]
                # total of the 3 pointers' list values
                total = n + left_val + right_val

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([n, left_val, right_val])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r+1]:
                        r -= 1
                    
        
        return res