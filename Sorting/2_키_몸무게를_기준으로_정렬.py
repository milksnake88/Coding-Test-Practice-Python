# n명의 이름, 키, 몸무게가 주어지면 키를 기준으로 오름차순으로 정렬하여 출력하는 프로그램

# 입력:
# 첫 번째 줄에는 n
# 두 번째 줄 부터는 n개의 줄에 걸쳐 이름, 키 몸무게가 공백을 사이에 두고 주어짐

# 출력: 키를 기준으로 오름차순 정렬, 키가 동일한 경우 몸무게가 더 큰 사람이 먼저

# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sort-by-height-and-weight/description

############################################################

class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
students = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    students.append(Student(name, int(height), int(weight)))

students.sort(key = lambda x:(x.height, -x.weight))

for student in students:
    print(student.name, student.height, student.weight)