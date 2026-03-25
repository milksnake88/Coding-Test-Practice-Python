# https://www.acmicpc.net/problem/14503

############################################################

from collections import deque

def bfs(sr, sc, sd):
    q = deque()

    q.append((sr, sc, sd))
    v[sr][sc] = 1
    cnt = 1

    while q:
        cr, cc, cd = q.popleft()
        found = False
        for _ in range(4):
            nd = (cd+3) % 4
            nr, nc = cr+move[nd][0], cc+move[nd][1]
            if arr[nr][nc]==0 and v[nr][nc] == 0:
                q.append((nr, nc, nd))
                v[nr][nc] = 1
                cnt += 1
                found = True
                break
            else:
                cd = nd
        if not found:
            if cd == 0:
                bd = 2
            elif cd == 1:
                bd = 3
            elif cd == 2:
                bd = 0
            else:
                bd = 1
            nr, nc = cr+move[bd][0], cc+move[bd][1]
            q.append((nr, nc, cd))
            if arr[nr][nc] == 1:
                return cnt

n, m = map(int, input().split())
r, c, d = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
move = [(-1,0), (0,1), (1,0), (0,-1)]
ans = bfs(r, c, d)
print(ans)