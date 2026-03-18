# 1. tuple을 이용한 객체 정렬

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

# Side Note: 문자열을 기준 정렬. 기본적으로 사전순 정렬을 한다

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
