# 문제 번호: 1952

############################################################

import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm):
    global ans 

    if ans<=sm:
        return
    
    if n>=12:
        ans = min(ans, sm)
        return
    
    dfs(n+1, sm+lst[n]*day) # 일간권
    dfs(n+1, sm+mon)        # 월간권
    dfs(n+3, sm+mon3)       # 분기권
    dfs(n+12, sm+year)      # 년간권

T = int(input())
for test_case in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = list(map(int, input().split()))

    # [1] 백트래킹 사용
    # ans = 31*12*3000
    # dfs(0, 0)

    # [2] 그리디한 방법(DP)
    D = [0]*13
    for i in range(1, 13):
        # 가능한 4가지 방법 중 i 달의 최소 비용
        mn = D[i-1]+lst[i]*day      # 일간권
        mn = min(mn, D[i-1]+mon)    # 월간권과 비교
        if i >=3:
            mn = min(mn, D[i-3]+mon3)
        if i >=12:
            mn = min(mn, D[i-12]+year) 
        D[i] = mn
    ans = D[12]

    print(f'#{test_case} {ans}')