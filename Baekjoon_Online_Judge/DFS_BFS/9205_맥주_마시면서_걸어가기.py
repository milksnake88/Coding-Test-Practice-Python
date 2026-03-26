# https://www.acmicpc.net/problem/9205

# [1] 편의점 위치 저장
# [2] ci,cj 기준으로 n개의 편의점 이동가능 확인(방문하지 않았던 위치에서 이동가능하냐)
# **조건**: for i (N): 미방문, 범위 내
#               if v[i] == 0, |cj-ni|+|cj-nj|<1000:
#                   Q삽입, v[]표시

############################################################

def bfs(si,sj,ei,ej):
    q = []
    v = [0]*N

    # 큐에 초기데이터 삽입, si,sj는 v에 표시 x. 편의점만
    q.append((si, sj))

    while q:
        ci,cj = q.pop(0)
        if abs(ci-ei)+abs(cj-ej)<=1000:
            return "happy"

        # 미방문 모든 편의점 좌표: 범위내인지 체크
        for i in range(N):
            if v[i]==0: # 방문하지 않은 편의점
                ni,nj = lst[i]
                if abs(ci-ni)+abs(cj-nj)<=1000: # 범위내
                    q.append((ni,nj))
                    v[i]=1

    return "sad"

TC = int(input())
for _ in range(TC):
    N = int(input())
    si, sj = map(int, input().split())
    lst = []
    for _ in range(N):
        ti, tj = map(int, input().split())
        lst.append((ti,tj))
    ei, ej = map(int, input().split())

    ans = bfs(si, sj, ei, ej)
    print(ans)