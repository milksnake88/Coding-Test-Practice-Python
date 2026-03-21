# https://www.acmicpc.net/problem/2644

############################################################

def bfs(s, e):
    q = []

    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        if c == e: # 목적지 찾음
            return v[e]-1 # 나와 한칸 떨어져있으면 1촌

        for n in adj[c]:
            if not v[n]:
                q.append(n)
                v[n] = v[c]+1

    # 이곳의 코드를 실행했다면... 찾지 못한 것!
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