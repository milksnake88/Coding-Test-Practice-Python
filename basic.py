# split()
# split()은 문자열을 특정 구분자로 나누어 리스트로 반환하는 메서드
# 기본적으로 공백을 구분자로 사용하지만, 다른 구분자를 지정할 수도 있음
input_str = input() # milk snake 88
input_split_list = input().split() # milk snake 88
print(input_str) # milk snake 88
print(input_split_list) # >> ['milk', 'snake', '88']

# list()
# list()는 반복 가능한 객체(문자열, 튜플, 집합 등)를 받아
# 새로운 리스트 객체를 생성하거나 빈 리스트를 만드는 내장 함수
print(list("hello")) # >> ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3))) # >> [1, 2, 3]
print(list(12345)) # >> 'int' object is not iterable

# map()
# map()은 각 요소에 함수를 자동으로 반복 적용해주는 함수
# 실제 값이 아니라 iterator
# map(int, "123")일 경우 내부적으로 [int('1'), int('2'), int('3')]
# list(map(int, "123")) => [1, 2, 3]

######## 실수 방지 ########
# 
# 함수 안에서 변수 재할당 주의!(https://sikaleo.tistory.com/99)

######## 엣지 케이스 ########
#
# 배열: 최솟값, 최댓값으로 값을 모두 맞춰서 풀어보기, 최소 크기, 최대 크기
# 정렬: 이미 정렬된 케이스, 역순 정렬된 케이스 만들어서 풀어보기

# 한 번도 변화가 안 일어나거나
# 첫 턴에 끝나거나
# 마지막 턴까지 가거나
# 동시에 여러 이벤트가 발생하는 경우