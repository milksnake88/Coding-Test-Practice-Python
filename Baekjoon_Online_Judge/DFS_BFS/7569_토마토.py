# https://www.acmicpc.net/problem/7569

# Hint: q에 초기데이터를 여러개 삽입할 수 있다..!
# [패턴]: 동시 다발적 -> q에 초기데이터 여러개 삽입
# 나중에 개수를 세야하는 건, 초반에 cnt로 세놓고 간다(지금처럼 최대 1000000번 loop 돌려야할 수도 있음)

# 모두 익는데 걸리는 날짜, 하나라도 못 익으면 -1 => 익지않은 개수 cnt

# bfs()
# 1. q생성, v[]생성
# 2. for h->i->j 전체 순회
#       1이면 초기데이터(들) 삽입, v[]<-1
#       0이면 cnt+=1
# while q:
# ch,ci,cj = q.pop(0)
# 6방향, 범위내, 미방문, arr==0:
#   q에 삽입, v[]<-v[c]+1
#   cnt -= 1
# if cnt==0:
#   return v[ch][ci][cj]-1
# else: return -1

############################################################

from collections import deque

def bfs():
    # [1] q 생성, v[]생성
    q = deque()
    v= [[[0]*M for _ in range(N)] for _ in range(H)]

    # [2] q에 초기데이터(들) 삽입, 안익은 토마토 카운트
    cnt = 0
    for h in range(H): # 전체순회하며 처리
        for i in range(N):
            for j in range(M):
                if arr[h][i][j]==1: # 익은 토마토
                    q.append((h,i,j))
                    v[h][i][j]=1
                elif arr[h][i][j]==0: # 안익은 토마토
                    cnt+=1
    while q:
        ch,ci,cj = q.popleft()
        
        # 6방향, 범위내, 미방문, arr==0
        for dh,di,dj in ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)):
            nh,ni,nj = ch+dh,ci+di,cj+dj
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and v[nh][ni][nj]==0 and arr[nh][ni][nj]==0:
                q.append((nh,ni,nj))
                v[nh][ni][nj] = v[ch][ci][cj]+1
                cnt -= 1
    if cnt == 0:
        return v[ch][ci][cj]-1
    else:
        return -1

M, N, H = map(int, input().split())

arr = []
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, input().split())))
    arr.append(layer)

ans = bfs()
print(ans)