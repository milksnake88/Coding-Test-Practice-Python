# https://www.acmicpc.net/problem/2573

# for year (1, 900000):
# [1] 둘러싼 0의 개수 카운트 sub array
# [2] 높이 낮추기: arr[i][j] = max(0, arr[i][j]-sub[i][j])
# [3] 덩어리 개수 카운트 (BFS)
#     cnt > 1 인 경우 -> return year
#     cnt == 0 인 경우 -> return 0

############################################################

from collections import deque

def bfs(si, sj, v):
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
            
def solve(): # 1~900000 년, 전체 순회 반복 작업
    for year in range(1, 900000):
        # [1] 네방향 0의 개수 카운트
        a_sub = [[0]*m for _ in range(n)]
        for i in range(1, n-1): # 가장자리는 방산 x
            for j in range(1, m-1):
                if arr[i][j]==0:
                    continue
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = i+di, j+dj
                    if arr[ni][nj] == 0:
                        a_sub[i][j] += 1
        
        # [2] 높이 낮추기
        # 한 루프보다 나눠서 짜는게 디버깅하기 편리하고 실수를 줄일 수 있음
        for i in range(1, n-1):
            for j in range(1, m-1):
                if a_sub[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j]-a_sub[i][j])
        
        # [3] 빙산 덩어리 개수 카운트
        v = [[0]*m for _ in range(n)]
        cnt = 0
        for ci in range(n-1):
            for cj in range(m-1):
                if arr[ci][cj] > 0 and not v[ci][cj]:
                    bfs(ci, cj, v)
                    cnt += 1
                    if cnt > 1: # 두 덩어리 이상... for문 안에다 체크해서 시간 아끼기
                        return year
        if cnt==0:
            return 0
    
    # 이 자리에 올 일은 없지만...
    return -1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = solve()
print(ans)



                
