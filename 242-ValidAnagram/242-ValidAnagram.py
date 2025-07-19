# Last updated: 7/19/2025, 4:36:29 PM
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) < len(t):
            return False
            
        smap = dict()
        tmap = dict()
        for char in s:
            smap[char] = smap.get(char, 0) + 1
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
        
       
        for k, v in smap.items():
            t_value = tmap.get(k, -1)
            if v != t_value:
                return False
        
        return True
        