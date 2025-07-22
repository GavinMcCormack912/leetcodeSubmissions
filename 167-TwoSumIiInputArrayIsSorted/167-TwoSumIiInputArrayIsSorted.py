# Last updated: 7/21/2025, 8:35:33 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #1, 2, 3, 5, 7, 9, 11, 15, etc
        idx1 = 0
        idx2 = len(numbers)-1

        while numbers[idx1] + numbers[idx2] != target:
            if numbers[idx1] + numbers[idx2] > target:
                idx2 -= 1
            
            elif numbers[idx1] + numbers[idx2] < target:
                idx1 += 1

        return [idx1+1, idx2+1]
        #go back and forth. reduce idx2 until num[idx1] + num[idx2] is < target
        # when that happens, increase idx1 until they're over. go back and forth
        #until the number is found. squeeze from both sides

