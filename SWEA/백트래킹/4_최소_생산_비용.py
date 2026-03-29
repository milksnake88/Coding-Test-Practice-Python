# 문제 번호: 5209

############################################################

def dfs(n, sm, v):
    global ans

    if ans<=sm:
        return 
    
    if n==N:
        ans = min(ans, sm)
        return
    
    for j in range(N):
        if j not in v:
            dfs(n+1, sm+arr[n][j], v+[j])

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 100*N
    # v = [0]*(N) -> 일반적으로 이 방법이 제일 빠르
    # v = []
    dfs(0,0,[])
    print(f'#{test_case} {ans}')