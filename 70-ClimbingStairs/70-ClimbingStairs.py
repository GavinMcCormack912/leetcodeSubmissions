# Last updated: 8/1/2025, 10:27:20 PM
class Solution:
    

    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1
        # each path at stairs n is equal to all the different numbers of path to stairs n-1 and n-2
        for i in range (n-1):
            temp = first
            first += second #going to third step
            second = temp # second is now at second's old value

        return first