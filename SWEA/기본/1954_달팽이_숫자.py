T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt_mx = N
    ci, cj = 0, -1
    dr = cnt = 0
    flag = 1

    for i in range(1, N*N+1):
        ci, cj = ci+di[dr], cj+dj[dr]
        arr[ci][cj] = i

        cnt+=1
        if cnt == cnt_mx:
            cnt = 0
            dr = (dr+1)%4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                cnt_mx -= 1
    print(f'#{test_case}')
    for lst in arr:
        print(*lst)