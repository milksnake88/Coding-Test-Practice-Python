# https://www.acmicpc.net/problem/2468

############################################################

def bfs(val, si, sj):
    q = []

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]>val:
                q.append((ni,nj))
                v[ni][nj] = 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = []

for val in range(0, 101):
    v = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > val and v[i][j] == 0:
                bfs(val, i, j)
                cnt += 1
    ans.append(cnt)

print(max(ans))