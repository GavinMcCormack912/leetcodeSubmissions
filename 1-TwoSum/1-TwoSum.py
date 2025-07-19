# Last updated: 7/19/2025, 4:36:32 PM
class Solution(object):
    def twoSum(self, nums, target):
        #anotha hashmap!
        numbers = {}
        # get list of indices in each number key
        for i in range(len(nums)):
            if nums[i] in numbers:
                numbers[nums[i]].append(i)
            else:  
                numbers[nums[i]] = [i]
        # check for complement. ensure it isn't a duplicate index
        for key, val in numbers.items():
            if target-key in numbers:
                if target-int(key) == key:
                    if len(numbers[key]) > 1:
                        ret_list = [numbers[key][0], numbers[key][1]]
                        ret_list.sort()
                        return ret_list
                else:
                    ret_list = [numbers[key][0], numbers[target-key][0]]
                    ret_list.sort()
                    return ret_list
                    
        
        return numbers
        