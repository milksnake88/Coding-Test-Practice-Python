# https://www.acmicpc.net/problem/2606

############################################################

# 1. dfs
def dfs(c):
    v[c] = 1

    for n in adj[c]:
        if not v[n]:
            dfs(n)

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

v = [0] * (N+1)
dfs(1)
print(sum(v)-1)

############################################################

# Trouble Shooting

"""
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)

가 틀린 이유:

* 이 문제의 연결은 무방향 연결이라서
* s에서도 e로 갈 수 있고 e에서도 s로 갈 수 있어야 하며
* 한쪽만 저장하면 입력 순서에 따라 탐색 가능 여부가 달라져서
* 실제 연결 관계를 제대로 표현하지 못하기 때문이야

ex 1)
입력이 만약 이렇게 들어오면:
2 1
5 2
6 5

adj[2] = [1]
adj[5] = [2]
adj[6] = [5]
adj[1] = []

로 1번에서 시작하면 아무 데도 못간다.

ex 2)
운 좋게 맞는 경우

입력:

N = 3
M = 2
1 2
2 3

(1) 양쪽 다 넣을 때
adj[1] = [2]
adj[2] = [1, 3]
adj[3] = [2]

dfs(1) 진행:

1 방문 2 방문 3 방문

방문 배열: v = [0, 1, 1, 1]

답: sum(v)-1 = 2

정답.

(2) 한쪽만 넣을 때
adj[1] = [2]
adj[2] = [3]
adj[3] = []

dfs(1) 진행:

1 방문 2 방문 3 방문

이 경우는 우연히 입력 방향이 1 -> 2 -> 3 형태라서 맞아.

즉, 항상 틀리는 건 아니고, 운 좋게 맞을 때도 있음.
"""
