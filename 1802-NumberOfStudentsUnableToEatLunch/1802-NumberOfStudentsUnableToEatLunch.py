# Last updated: 8/1/2025, 10:27:10 PM
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # sandwiches[-1] is top of stack
        # students[0] is front of the queue
        students0 = 0
        students1 = 0

        sandwiches0 = 0
        sandwiches1 = 0

        for s in students:
            if s == 1:
                students1 += 1
            else:
                students0 += 1
        
        for i in range(len(sandwiches)):
            sd = sandwiches[i]
            if sd == 0 and students0 > 0:
                students0 -= 1
            elif sd == 1 and students1 > 0:
                students1 -= 1
            else:
                break


        return students0 + students1