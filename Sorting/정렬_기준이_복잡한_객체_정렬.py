############################################################

# 정렬 기준이 멤버 변수가 아닌 경우, 원하는 기준 값을 반환해주도록 lambda 함수의 반환 값을 설정

# lambda로 처리하기 애매한 경우에는 lambda 함수 대신 직접 기준을 정해주는 comparator 함수를 만들어줘야 함
# python3에서는 이 함수를 sort함수의 key인자로 넘길때 꼭, functools내 cmp_to_key 함수를 import하여 com_to_key(compare)식으로 감싸줘야 함

# 정렬 기준을 나타내는 함수인 compare 함수는 2개의 인자를 설정해줘야 함

# x가 앞에 있는 원소, y가 뒤에 있는 원소라 가정했을 때
# 둘의 순서가 우리가 원하는 순서라면 0보다 작은 값을,
# 반대라면 0보다 큰 값을,
# 둘의 우선순위가 동일하다면 0을 반환
# 보통 -1, 1, 0을 사용

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

# 점수의 총합 기준 오름차순
students.sort(key=lambda x : x.kor + x.eng + x.math)

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)

# >> 80 20 10
#    60 10 50
#    20 80 80
#    90 30 60
#    90 80 90

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
students.sort(key=lambda x : x[0] + x[1] + x[2])

for kor, eng, math in students:
    print(kor, eng, math)

# >> 80 20 10
#    60 10 50
#    20 80 80
#    90 30 60
#    90 80 90

############################################################

# 3. Side Note: 복잡한 기준을 갖는 정렬

# 국어 점수를 기준으로 정렬하되, 국어 점수가 30의 배수인 경우가 먼저 나오게 하고 싶다고 생각해보자

from functools import cmp_to_key

students = [
    Student(90, 80, 90), # 첫 번째 학생
    Student(20, 80, 80), # 두 번째 학생
    Student(90, 30, 60), # 세 번째 학생
    Student(60, 10, 50), # 네 번째 학생
    Student(80, 20, 10), # 다섯 번째 학생 
]

# custom comparator를 직접 정의
def compare(x, y):
    # x만 30의 배수라면 x가 더 앞에 있어야 하므로
    # 현재 순서가 옳습니다.
    if x.kor % 30 == 0 and y.kor % 30 != 0:
        return -1
    # y만 30의 배수라면 y가 더 앞에 있어야 하므로
    # 현재 순서는 틀렸습니다.
    if x.kor % 30 != 0 and y.kor % 30 == 0:
        return 1
    # 우선 순위가 동일한 경우입니다.
    return 0

# compare 기준에 따른 custom 정렬
students.sort(key=cmp_to_key(compare))

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)

# >> 90 80 90
#    90 30 60
#    60 10 50
#    20 80 80
#    80 20 10

