# Last updated: 7/21/2025, 8:35:31 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # basically, I need to find the minimum k where I will spend a total
        # number of hours eating the bananas from each pile. Think of an hour like a "round"
        # O(n logm) preferred. So basically, use binary search on banana size
        # and go through the pile each time to check. start with max num of bananas
        # in a pile, and 1

        under = 1
        over = max(piles)

        # use this to get an estimate, then try subtracting bananas after to see if you can
        # be a little more efficient
        k = over
        while under <= over:
            hrs = 0
            bananas = (under + over) // 2

            for pile in piles:
                hrs += math.ceil(pile/bananas)
            #make it decrease as long as possible. get lowest number of bananas
            if hrs <= h:
                k = bananas
                over = bananas - 1 #lower top pointer
            else:
                #if not enough bananas, increase lower pointer
                under = bananas + 1
        return k
        