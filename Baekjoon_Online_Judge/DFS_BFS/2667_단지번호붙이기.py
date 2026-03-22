# https://www.acmicpc.net/problem/2667

# bfs, dfs 둘 다 풀어도 되는 문제
# map이 커지면 재귀호출의 제한도 있고, bfs가 성능 상 더 빠르기 때문에
# 커지는데.. 싶으면 bfs로 

# 손코딩

# ans = []
# arr 배열 순회 "방문하지 않은 1을 만나면"
# for i (N)
#   for j (N)
#       if arr[i][j]==1 and v[i][j]==0
#           ans.append(bfs(i,j))
# ans 오름차순 정렬
# print(len(ans), *ans, sep="\n")

# bfs(si, sj):
#   q 등 생성
#   q에 데이터 삽입, v[]표시, cnt=1: 단위 작업
#   while q:
#       ci, cj <- q
#       4방향, 범위 내, 조건(미방문, 1이면)
#           단위 작업

############################################################

# bfs: 시작위치 받아서, 해당 위치에 연결된 1의 개수 리턴
def bfs(si, sj):
    q = [] # q 등 필요 변수 생성

    v[si][sj] = 1 # 방문표시
    q.append((si, sj)) # 큐 초기데이터 삽입
    cnt = 1 # 정답처리 관련 작업

    while q:
        ci, cj = q.pop(0)    

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            # 4방향, 범위내, 미방문, 1이면 q 삽입
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and adj[ni][nj]==1:
                v[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
    return cnt
    

N = int(input())

adj = []
for _ in range(N):
    adj.append(list(map(int, input())))

ans = []
v = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 방문하지 않았던 아파트 발견시 bfs
        if adj[i][j] == 1 and v[i][j]==0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans), *ans, sep='\n')
