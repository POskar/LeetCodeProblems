#1700. Number of Students Unable to Eat Lunch

from typing import List


def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    while len(students) > 0:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
        else:
            if sandwiches[0] in students:
                students.append(students[0])
                students.pop(0)
            else:
                break
    return len(students)


students, sandwiches = [1,1,1,0,0,1], [1,0,0,0,1,1]
print(countStudents(0, students, sandwiches))