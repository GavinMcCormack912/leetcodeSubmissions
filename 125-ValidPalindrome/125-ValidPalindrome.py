# Last updated: 7/19/2025, 4:38:02 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        for char in s.lower():
            if char.isalnum():
                st.append(char)
        n = len(st)
        end = n-1
        start = 0

        while start < end and st[start] == st[end]:
            start += 1
            end -= 1
        
        if start == end:
            if st[start] != st[end]:
                return False
            return True

        if start < end:
            return False
        return True