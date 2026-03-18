############################################################

# 0. 객체 정렬을 사용하는 이유

# 다음과 같이 학생의 국어, 영어, 수학 점수를 다 따로 관리할 경우
kors = [90, 20, 90, 60, 80]
engs = [80, 80, 30, 10, 20]
maths = [90, 80, 60, 50, 10]

# 국어 점수만 정렬될 수 있다

kors.sort() 

print(kors)  # >> [20, 60, 80, 90, 90]
print(engs)  # >> [80, 80, 30, 10, 20]
print(maths) # >> [90, 80, 60, 50, 10]

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

# lambda 함수의 x인자에 들어오는 값은 하나의 객체
students.sort(key=lambda x : x.kor) # 국어 점수 기준 오름차순 정렬

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)

# >> 20 80 80
#    60 10 50
#    80 20 10
#    90 80 90
#    90 30 60

students.sort(key=lambda x : -x.kor) # 국어 점수 기준 내림차순 정렬

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)

# >> 90 80 90
#    90 30 60
#    80 20 10
#    60 10 50
#    20 80 80

############################################################

# 2. tuple을 이용한 객체 정렬

students = [
    (90, 80, 90), # 첫 번째 학생
    (20, 80, 80), # 두 번째 학생
    (90, 30, 60), # 세 번째 학생
    (60, 10, 50), # 네 번째 학생
    (80, 20, 10), # 다섯 번째 학생 
]

# lambda 함수의 x인자에 들어오는 값은 하나의 tuple
students.sort(key=lambda x : x[0]) # 국어 점수 기준 오름차순 정렬

for kor, eng, math in students: 
    print(kor, eng, math)

# >> 20 80 80
#    60 10 50
#    80 20 10
#    90 80 90
#    90 30 60

students.sort(key=lambda x : -x[0]) # 국어 점수 기준 내림차순 정렬

# for student in students:
#     kor, eng, math = student
#     print(kor, eng, math)

for kor, eng, math in students: # unpacking을 for loop와 함께
    print(kor, eng, math)

# >> 90 80 90
#    90 30 60
#    80 20 10
#    60 10 50
#    20 80 80

############################################################

# 3. Side Note: 문자열을 기준으로 정렬하기. 기본적으로 사전순 정렬을 한다

students = [
    ("lee", 80, 90), # 첫 번째 학생
    ("kim", 80, 80), # 두 번째 학생
    ("park", 30, 60), # 세 번째 학생
]

students.sort(key=lambda x: x[0]) # 이름 기준 사전순 정렬

for name, eng, math in students: # 정렬 이후의 결과 출력
    print(name, eng, math)

# >> kim 80 80
#    lee 80 90
#    park 30 60