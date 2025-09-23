# Last updated: 9/23/2025, 11:45:36 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # python dict retaining the numbers in the list
        numList = {}
        freqList = [[] for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            numList[nums[i]] = numList.get(nums[i], 0) + 1
        
        for key, val in numList.items():
            freqList[val].append(key)
        
        res = []
        for i in range(len(freqList)-1, -1, -1):
            if freqList[i]:
                for n in freqList[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
        
        return res

