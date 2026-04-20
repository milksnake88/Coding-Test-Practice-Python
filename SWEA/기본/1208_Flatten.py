import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    # 내 풀이
    # for i in range(N+1):
    #     mx = max(lst)
    #     mn = min(lst)
    #     if (mx-mn)==0 or (mx-mn)==1:
    #         break
    #     mxidx = lst.index(mx)
    #     mnidx = lst.index(mn)
    #     lst[mxidx] = mx-1
    #     lst[mnidx] = mn+1
    # print(f'#{test_case} {mx-mn}')

    # 문어 선생님 풀이
    ans = 100
    for _ in range(N):
        lst.sort()
        lst[0] += 1
        lst[-1] -= 1
        if ans > max(lst)-min(lst):
            ans = max(lst)-min(lst)

    print(f'#{test_case} {ans}')

