# Last updated: 7/19/2025, 4:36:31 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        start = [""]*(2 * n)
        openpars = n
        closedpars = n

        # use stacks to check that there are remaining open and closed parentheses
        # try ( or ) at every position. disallow if open parentheses aren't left over or 
        # there aren't enough used for a closer parenthesis
        retArr = []
        def get_arr(arr: List[str], loops: int, opens: int, closed: int):
            if loops <= 0:
                retArr.append("".join(arr))
                return
            else:
                closedarr = arr.copy()
                openarr = arr.copy()
                if closed > 0 and closed > opens:
                    closedarr[-loops] = ")"
                    closed_left = closed - 1
                    new_loops = loops - 1
                    get_arr(closedarr, new_loops, opens, closed_left)
                if opens > 0:
                    openarr[-loops] = "("
                    opens_left = opens - 1
                    new_loops = loops - 1
                    get_arr(openarr, new_loops, opens_left, closed)
                else:
                    print(arr)
        # send to res
        get_arr(start, n*2, openpars, closedpars)
        return retArr