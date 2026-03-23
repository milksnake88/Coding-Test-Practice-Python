# https://www.acmicpc.net/problem/7569

# Hint: q에 초기데이터를 여러개 삽입할 수 있다..!
# [패턴]: 동시 다발적 -> q에 초기데이터 여러개 삽입
############################################################

from collections import deque

def bfs():
    if not q:
        return -1
    while q:
        ch,ci,cj = q.popleft()

        for dh,di,dj in ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)):
            nh,ni,nj = ch+dh,ci+di,cj+dj
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and v[nh][ni][nj]==0 and arr[nh][ni][nj]==0:
                q.append((nh,ni,nj))
                v[nh][ni][nj] = v[ch][ci][cj]+1
                arr[nh][ni][nj] = 1
    return v[ch][ci][cj]-1

def print_ans(ans):
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j]==0:
                    return print(-1)
    return print(ans)

M, N, H = map(int, input().split())

arr = []
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, input().split())))
    arr.append(layer)

v= [[[0]*M for _ in range(N)] for _ in range(H)]

q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j]==1 and v[h][i][j]==0:
                q.append((h, i, j))
                v[h][i][j] = 1
ans = bfs()
print_ans(ans)