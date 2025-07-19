# Last updated: 7/19/2025, 4:36:28 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep track of current numbers. combine them with an operator with needed. left to right
        numStack = []
        #remaining value will be left in numStack[0]
        operators = "-+*/"
        #check if an operator, else it's an integer
        for token in tokens:
            if token in operators:
                if token == "-":
                    minus = numStack.pop()
                    new_top = numStack.pop() - minus
                    numStack.append(new_top)
                elif token == "+":
                    plus = numStack.pop()
                    new_top = numStack.pop() + plus
                    numStack.append(new_top)
                elif token == "*":
                    mult = numStack.pop()
                    new_top = numStack.pop() * mult
                    numStack.append(new_top)
                else:
                    div = numStack.pop()
                    new_top = int(numStack.pop() / div)
                    numStack.append(new_top)
            # add to numStack
            else:
                numStack.append(int(token))
        
        return numStack[0]
