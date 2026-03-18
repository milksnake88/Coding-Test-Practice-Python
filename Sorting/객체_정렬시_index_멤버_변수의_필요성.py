############################################################

# 0. enumerate() 사용하기

# enumerate() → (idx, element) 구조
# enumerate()를 사용하면 인덱스와 원소를 동시에 접근하면서 루프 돌리기
# for 문의 in 뒷 부분을 enumerate() 함수로 한 번 감싸주기만 하면 된다.

for entry in enumerate(['A', 'B', 'C']):
   print(entry)
 
# >> (0, 'A')
#    (1, 'B')
#    (2, 'C')

# enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플을 만들어준다. 
# 따라서 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 인자 풀기를 해줘야 한다.
# start값을 인자로 넘기면 시작 index값을 설정할 수 있다.

for i, letter in enumerate(['A', 'B', 'C'], start=1):
   print(i, letter)
# 
# >> 1 A
#    2 B
#    3 C

############################################################

# 1. class를 이용한 객체 정렬

class Student:
    def __init__(self, kor, eng, math, number):
        self.kor = kor
        self.eng = eng
        self.math = math
        self.number = number

students = [
    Student(90, 80, 90, 1), # 첫 번째 학생
    Student(20, 80, 80, 2), # 두 번째 학생
    Student(90, 30, 60, 3), # 세 번째 학생
    Student(60, 10, 50, 4), # 네 번째 학생
    Student(80, 20, 10, 5), # 다섯 번째 학생 
]

students.sort(key=lambda x : -x.kor) # 국어 점수 기준 내림차순 정렬

# 정렬 이후 등수별 학생 번호 출력
for idx, student in enumerate(students, start=1):
    print(f"{idx}등: {student.number}번")

# >> 1등: 1번
#    2등: 3번
#    3등: 5번
#    4등: 4번
#    5등: 2번

############################################################

# 2. tuple을 이용한 객체 정렬

students = [
    (90, 80, 90, 1), # 첫 번째 학생
    (20, 80, 80, 2), # 두 번째 학생
    (90, 30, 60, 3), # 세 번째 학생
    (60, 10, 50, 4), # 네 번째 학생
    (80, 20, 10, 5), # 다섯 번째 학생 
]

students.sort(key=lambda x : -x[0]) # 국어 점수 기준 내림차순 정렬

# enumerate로 뽑아낸 tuple값에서 kor, eng, math는 필요 없고 4번째 값인 number 값만 필요
# 나머지는 _로 처리

# enumerate(students)가 반환하는 값은 이렇게 생김: (idx, (90, 80, 90, 1))
# 그래서 구조는 이렇게 풀림: idx, (a, b, c, number)
# 즉 (a, b, c, number)를 구조 분해하려면 괄호가 필요함
# 잘못된 경우: for idx, a, b, c, d in enumerate(students):
# 파이썬은 이렇게 이해함; (idx, a, b, c, d)

for idx, (_, _, _, number) in enumerate(students, start=1):
    print(f"{idx}등: {number}번")

# >> 80 20 10
#    60 10 50
#    20 80 80
#    90 30 60
#    90 80 90

############################################################

# 3. Side Note: 정렬 이후 각 번호가 어디로 갔는지를 출력하는 코드

# 등수 별 학생 번호인 1 3 5 4 2 가 주어졌을 때, 각 학생별 등수인 1 5 2 4 3 을 쉽게 구하기

# 어느 학생이 어떤 등수를 받았는지를 나타내는 배열을 새로 하나 만들어 이용하면 된다.
# 등수 별 학생 번호를 순회하면서, 각 학생 번호의 index에 해당 rank를 넣어주는 식으로 코드를 작성

num_to_rank = [0] * 6

nums = [1, 3, 5, 4, 2]

for rank, num in enumerate(nums, start=1):
    num_to_rank[num] = rank

print(num_to_rank) # >> [0, 1, 5, 2, 4, 3]
