# https://www.acmicpc.net/problem/2468

# 영역의 개수: 네방향, 범위 내, 미방문, >H
# 0부터 99까지 비가 온 높이별로 영역개수 구해서 최댓값 찾기
# ans=0, h:0~99 바꾸면서 최댓값 구하기
# solve(h)
#   cnt = 0
#   for i (N)
#       for j (N)
#           if v[i][j]==0 and arr[i][j] > h:
#               bfs(i, j), cnt+=1
#   return cnt

# 4방향, 범위내 0<= <N, v[ni][nj]==0, arr[ni][nj]>h:
#   q삽입, v표시
############################################################

from collections import deque
def bfs(h, si, sj):
    q = deque()

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        # 네방향, 범위내, 미방문, 높이>h
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]>h:
                q.append((ni,nj))
                v[ni][nj] = 1

def solve(h): # h높이에 대해 잠기지 않는 영역 개수 리턴
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and v[i][j] == 0:
                bfs(h, i, j)
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for h in range(100): # 높이 0 ~ 99 까지 물 높이 지정
    v = [[0]*N for _ in range(N)]
    ans = max(ans, solve(h))

print(ans)