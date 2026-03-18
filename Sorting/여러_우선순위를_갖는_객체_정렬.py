############################################################

# 0. tuple의 특성

# 여러 우선순위를 갖는 경우에는, lambda 함수의 반환값을 단일 값이 아닌, tuple 값으로 정의한다.

# tuple은 비교 연산 시, 첫 번째 원소를 기준으로 먼저 비교를 하고, 첫 번째 원소가 동일하다면 두 번째 원소를 기준으로 비교한다.

print((2, 3) > (1, 9)) # >> True
print((2, 3) > (2, 8)) # >> False
print((2, 3) > (3, 1)) # >> False

# 이러한 tuple의 특성을 이용하여 lambda 함수의 반환값에 우선순위대로 각 기준이 되는 값을 적어주면 된다.

############################################################

# 1. class를 이용한 객체 정렬

class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

students = [
    Student(90, 80, 90), # 첫 번째 학생
    Student(20, 80, 80), # 두 번째 학생
    Student(90, 30, 60), # 세 번째 학생
    Student(60, 10, 50), # 네 번째 학생
    Student(80, 20, 10), # 다섯 번째 학생 
]

# 첫 번째 우선순위는 국어 점수 오름차순
# 국어 점수가 같다면 두 번째 우선순위는 영어 점수 오름차순
students.sort(key=lambda x : (x.kor, x.eng))

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)

# >> 20 80 80
#    60 10 50
#    80 20 10
#    90 30 60
#    90 80 90

# 국어 점수는 오름차순, 국어 점수가 동일한 경우 영어 점수는 내림 차순
students.sort(key=lambda x : (x.kor, -x.eng))

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)

# >> 20 80 80
#    60 10 50
#    80 20 10
#    90 80 90
#    90 30 60

############################################################

# 2. tuple을 이용한 객체 정렬

students = [
    (90, 80, 90), # 첫 번째 학생
    (20, 80, 80), # 두 번째 학생
    (90, 30, 60), # 세 번째 학생
    (60, 10, 50), # 네 번째 학생
    (80, 20, 10), # 다섯 번째 학생 
]

# 첫 번째 우선순위는 국어 점수 오름차순
# 국어 점수가 같다면 두 번째 우선순위는 영어 점수 내림차순
students.sort(key=lambda x : (x[0], -x[1]))

for kor, eng, math in students:
    print(kor, eng, math)

# >> 20 80 80
#    60 10 50
#    80 20 10
#    90 80 90
#    90 30 60