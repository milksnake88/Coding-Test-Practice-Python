# https://www.acmicpc.net/problem/1697

############################################################

def bfs(s, e):
    q = []
    v = [0 for _ in range(100002)]

    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        if c == e:
            return v[c]-1
        # 3방향, 범위내, 미방문, (조건)
        for n in (c-1, c+1, 2*c):
            if 0<=n<=100000 and not v[n]:
                q.append(n)
                v[n] = v[c] + 1

    return -1

n, k = map(int, input().split())

ans = bfs(n, k)
print(ans)