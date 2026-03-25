# https://www.acmicpc.net/problem/2573

############################################################

from collections import deque

def bfs(si, sj):
    q = deque()

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]>0 and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = 1
            
def solve():
    global v
    cnt_years = 0
    while True:
        cnt_zero = 0
        cnt_bfs = 0
        ice = [[0]*m for _ in range(n)]
        for ci in range(n):
            for cj in range(m):
                if arr[ci][cj] <= 0:
                    cnt_zero += 1
                else:
                    ice[ci][cj] = 1
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<n and 0<=nj<m and arr[ni][nj] <= 0 and not ice[ni][nj]:
                        arr[ci][cj] -= 1
        if cnt_zero == n*m:
            return 0
        v = [[0]*m for _ in range(n)]
        for ci in range(n):
            for cj in range(m):
                if arr[ci][cj] > 0 and not v[ci][cj]:
                    bfs(ci, cj)
                    cnt_bfs += 1
        cnt_years += 1
        if cnt_bfs >= 2:
            return cnt_years

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
        
print(solve())



                
