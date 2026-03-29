# 문제 번호: 4881

# 가능한 모든 경우

# n: 행 번호
# 열 번호는 가지에!
# 트리를 그릴 때 일반화해서 그리기!
############################################################

def dfs(n, sm):
    global ans
    if ans<=sm: # 최소 합 문제에서 항상 사용할 수 있는 가지치기
        return 
    
    if n==N:
        ans = min(ans, sm)
        return
    
    for j in range(N):
        if v[j]==0:
            v[j]=1
            dfs(n+1, sm+arr[n][j])
            v[j]=0  # 잊지 마세요!!!

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))

    ans = N*10
    v = [0]*N
    dfs(0, 0)

    print(f'#{test_case} {ans}')