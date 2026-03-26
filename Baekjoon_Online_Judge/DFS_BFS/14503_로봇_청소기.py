# https://www.acmicpc.net/problem/14503

# dr 북 동 남 서
# di [-1, 0, 1, 0]
# dj [0, 1, 0, -1]

# 시뮬레이션 문제: 길더라도 시키는대로 동작을 최대한 해보고, 다시한번 재정의하기

# [1] 현재 위치 청소: arr[ci][cj] <- 2, cnt+=1
# [2] 왼쪽 방향부터 4방향 탐색
#   for 빈 곳: arr[ni][nj] == 0
#       새로운 방향, 좌표 갱신
#   else 
#       후진할 위치가 벽이 아님: 후진
#       벽: 종료

############################################################

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def solve(cr,cc,d):
    cnt = 0 # 청소한 공간 수
    while 1: # 청소기가 더이상 움직이지 못할 때 종료
        # [1] 현재위치 청소
        arr[cr][cc] = 2
        cnt+=1
        # [2] 왼쪽방향으로 순서대로 탐색해서 미청소 영역이 있는 경우 이동/방향설정, 없으면 후진
        flag = 1
        while flag==1:
            # 왼쪽부터 네방향 중 미청소 영역이 있는 경우
            for nd in ((d+3)%4, (d+2)%4, (d+1)%4, d):
                nr, nc = cr+di[nd], cc+dj[nd]
                if arr[nr][nc]==0: # 미청소 영역
                    cr, cc, d = nr, nc, nd
                    flag = 0
                    break
            else: # 4방향 모두 미청소 영역 없음 ==> 후진
                br,bc = cr-di[d], cc-dj[d] # 상하좌우 전진이 더해주는 거니까 후진은 빼주면 됨
                if arr[br][bc] == 1:
                    return cnt
                else:
                    cr, cc = br, bc
    # 이 곳에 도달할리는 없지만...
    return -1

n, m = map(int, input().split())
r, c, d = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = solve(r,c,d)
print(ans)