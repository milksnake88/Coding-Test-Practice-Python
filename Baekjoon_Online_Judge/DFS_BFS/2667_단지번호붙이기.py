# https://www.acmicpc.net/problem/2667

############################################################

def bfs(si, sj):
    cnt = 1
    q = []

    v[si][sj] = 1
    q.append((si, sj))

    while q:
        ci, cj = q.pop(0)    

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and adj[ni][nj]==1:
                v[ni][nj] = 1
                adj[ni][nj] = adj[ci][cj] + 1
                q.append((ni, nj))
                cnt += 1
    return cnt
    

N = int(input())

adj = []
for _ in range(N):
    adj.append(list(map(int, input())))

num = []
v = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if adj[i][j] == 1:
            ans = bfs(i, j)
            num.append(ans)

num.sort()
print(len(num))
for i in range(len(num)):
    print(num[i])
