# Last updated: 7/19/2025, 4:36:32 PM
class Solution:
    def isValid(self, s: str) -> bool:
        #need to check ) } ] don't come first
        #check they come in right order. LIFO ---> stack
        order = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            #ensure brackets dont close without opening brackets
            if char in order:
                if stack and order[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        #check stack is empty. no opening brackets, parentheses, etc. left behind
        if stack:
            return False
        return True
