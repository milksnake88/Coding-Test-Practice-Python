# https://www.acmicpc.net/problem/2644

############################################################

def bfs(s, e):
    q = []
    q.append((0, s))
    v[s] = 1

    while q:
        c = q[0][1]
        cnt = q[0][0]
        q.pop(0)
        if c == e:
            return cnt
    
        for n in adj[c]:
            if not v[n]:
                q.append((cnt+1, n))
                v[n] = 1

    return -1

n = int(input())
s, e = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

v = [0] * (n+1)

ans = bfs(s, e)
print(ans)