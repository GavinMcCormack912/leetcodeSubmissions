# Last updated: 7/21/2025, 8:35:35 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = len(matrix) - 1
        bottom = 0
        width = len(matrix[0]) - 1
        #binary search the row, then use binary search for target on the specific row
        #O(logn) + O(logn) = O(2 * logn) = O(logn)

        #get row
        row = matrix[0]
        found = False
        while bottom <= top:
            middle_row = (top+bottom) // 2
            row = matrix[middle_row]
            # if target is less than the start of the row, its in an earlier row
            if target < row[0]:
                print(row[width])
                top = middle_row - 1 

            #if the target is greater than the end of the row, it's in a later row
            elif target > row[width]:
                bottom = middle_row + 1
            #else, end loop. we got the right row now
            else:
                found = True
                break
        #if a row wasn't found, it doesn't exist. return False
        if not found:
            #print("No row found")
            return False

        #we're at the right row now. Now, use classic binary search
        left = 0
        right = width

        while left <= right:
            middle = (left + right) // 2

            if target > row[middle]:
                left = middle + 1
            elif target < row[middle]:
                right = middle - 1
            else:
                return True
        
        return False