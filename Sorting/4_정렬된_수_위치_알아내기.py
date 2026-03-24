# 양의 정수를 원소로 갖는 길이가 N인 수열이 입력으로 주어졌을 때, 
# 이 수열을 오름차순으로 정렬했을 때 각각의 위치에 있던 원소가 어느 위치로 이동하는지 출력하는 코드

# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-indices-of-sorted-array/description

############################################################

n = int(input())
nums = list(map(int, input().split()))

list = []
for i, num in enumerate(nums):
    list.append((num, i))

list.sort(key=lambda x:x[0])

ans = [0]*n

for i in range(n):
    ans[list[i][1]] = i+1

print(*ans)

############################################################

# 클래스 선언
class Number:
    def __init__(self, number, index):
        self.number, self.index = number, index


# 변수 선언 및 입력
n = int(input())
numbers = []
arr = list(map(int, input().split()))
numbers = [
    Number(num, i)
    for i, num in enumerate(arr)
]
answer = [
    0 for _ in range(n)
]

# Custom Comparator를 활용한 정렬
numbers.sort(key=lambda x: (x.number, x.index))

# 정렬된 숫자들의 원래 인덱스를 활용한 정답 배열 저장
for i, number in enumerate(numbers):
    answer[number.index] = i + 1 # 인덱스 보정

# 출력
for i in range(n):
    print(answer[i], end = ' ')




