# https://www.codetree.ai/ko/trails/complete/curated-cards/test-line-up-students-2/description

############################################################

class Student:
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n
        
n = int(input())

students = []

for i in range(n):
    h, w = map(int, input().split())
    students.append(Student(h, w, i+1))

students.sort(key=lambda x: (x.h, -x.w))

for student in students:
    print(student.h, student.w, student.n)