# 2차 평면 위에 N개의 점이 주어졌을 때, 원점에서 가까운 점부터 순서대로 번호를 출력하는 프로그램

# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-distance-from-origin/description

############################################################

# 변수 선언 및 입력:
n = int(input())
distances = list()


# 원점과의 거리를 계산하는 함수입니다.
def get_dist_from_origin(x, y):
    return abs(x) + abs(y)


for i in range(n):
    x, y = tuple(map(int, input().split()))
    # 원점과의 거리와 index를 저장합니다.
    distances.append((
        get_dist_from_origin(x, y), i + 1
    ))

distances.sort()

for _, idx in distances:
    print(idx)



