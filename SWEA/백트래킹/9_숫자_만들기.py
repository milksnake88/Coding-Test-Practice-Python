# 문제 번호: 4008

############################################################

import sys
sys.stdin = open("input.txt", "r")

def dfs(n, num, add, sub, mul, div):
    global mn, mx

    if n==N:
        mn = min(mn, num)
        mx = max(mx, num)
        return

    if add:
        dfs(n+1, num+lst[n], add-1, sub, mul, div)
    if sub:
        dfs(n+1, num-lst[n], add, sub-1, mul, div)
    if mul:
        dfs(n+1, num*lst[n], add, sub, mul-1, div)
    if div:
        dfs(n+1, int(num/lst[n]), add, sub, mul, div-1)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    lst = list(map(int, input().split()))

    mn = int(1e8)
    mx = int(-1e8)
    dfs(1, lst[0], add, sub, mul, div)
    print(f'#{test_case} {mx-mn}')
