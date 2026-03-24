# 5명의 이름, 키, 몸무게가 주어지면 이름순으로 정렬하여 출력하고, 키가 큰 순으로 정렬하여 출력하는 프로그램

# 입력: 5줄에 걸쳐 이름, 키, 몸무게가 공백을 사이에 두고 주어짐. 몸무게 값은 실수
# 출력: 이름순으로 정렬하여 출력, 키가 큰 순으로 정렬하여 출력. 몸무게 값은 소수점 첫째자리까지 출력

# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-personal-info/description

############################################################

# 클래스 선언
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

# 변수 선언 및 입력
students = []
for _ in range(5):
    name, height, weight = tuple(input().split())
    students.append(Student(name, int(height), float(weight)))

# Custom Comparator를 활용한 정렬 (이름순으로 정렬)
students.sort(key=lambda x: x.name)

print("name")
# 이름순으로 정렬한 결과 출력
for student in students:
    print(student.name, student.height, student.weight)

print()

# Custom Comparator를 활용한 정렬 (키순으로 정렬)
students.sort(key=lambda x: -x.height)

print("height")
# 키순으로 정렬한 결과 출력
for student in students:
    print(student.name, student.height, student.weight)