# https://www.acmicpc.net/problem/1260

# 정점 번호가 작은 것 먼저 방문 -> adj의 각 노드를 오름차순 정렬!

############################################################

# DFS
# 1. dfs(c)가 방문해서 해야할 단위 작업
# 1-1. 방문 표시: v[c] = 1 (current 노드에 방문 표시)
# 1-2. 정답 추가: ans_dfs.append(c) (answer에 방문한 current 노드 추가)

# 2. 방문: next 노드를 꺼내오고, next 노드가 가보지 않은 곳이라면 dfs(n)으로 노드 방문

# dfs(c)
# v[c] = 1, ans_dfs.append(c) # 해야할 일
# for n in adj[n]: # 방문
#     if v[n] == 0:
#         dfs(n)

############################################################

# BFS
# 1. q, v, 변수 생성
# 2. 해야할 단위 작업: q에 초기데이터(들) 삽입, v[]표시, ans 처리
# while q: 
#   q에서 데이터 한개 꺼냄
#   for 네 방향, 8 방향 ... **조건** 맞으면 Q 삽입

############################################################

# Main
# v = [0] * (N+1), ans = []
# dfs(v)

############################################################

def dfs(c):
    # 단위 작업
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1 # 방문 표시

    for n in adj[c]:
        if not v[n]: # next 노드가 아직 방문하지 않은 곳이라면
            dfs(n)

def bfs(s):
    q = [] # 필요한 q, v[], 변수 생성

    q.append(s) # Q에 초기데이터(들) 삽입
    # 단위 작업
    ans_bfs.append(s)
    v[s] = 1 # 방문 표시

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]: # 방문하지 않은 노드 => 큐 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향

# 1. 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0] * (N+1)
ans_dfs = []
dfs(V)

v = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)