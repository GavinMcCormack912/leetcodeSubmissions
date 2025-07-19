# Last updated: 7/19/2025, 4:36:30 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a dict of lists. key is letter counts. values are the list of strings
        anagrams = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]


        
        return list(anagrams.values())
