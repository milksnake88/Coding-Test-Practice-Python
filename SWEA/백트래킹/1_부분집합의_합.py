# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# 문제 번호: 4837 

# 백트래킹: 가능한 모든 경우 처리 => 반드시 정답이 나옴. 시간초과 주의!

# tree로 표현한다 (n이라는 발전시켜나가는 단계를 O안에)
# n: 보통 배열의 index(숫자 위치). **종료조건에 관련**
# **정답은 종료시에만 처리!**

# dfs(n, 필요시 추가: sm, cnt)
#   종료조건(n에 관련)
#   if n==N:
#       if sm==K and CNT==cnt:
#           ans+=1
#       return
#   
#   사용한 경우
#   dfs(n+1, sm+lst[n], cnt+1)
#   사용하지 않은 경우
#   dfs(n+1, sm, cnt)

############################################################

def dfs(n, sm, cnt):
    global ans
    # 가지치기: 가장 마지막에 고민... 가장 위에 처리
    if sm>K:    # 이미 초과.. 음수가 없으므로..
        return

    # 종료조건: n에 관련된 수식. 정답은 이 안에서만 처리
    if n==N:
        if sm==K and cnt==CNT:
            ans += 1
        return
    
    dfs(n+1, sm+lst[n], cnt+1) # 사용하는 경우
    dfs(n+1, sm, cnt) # 사용하지 않는 경우

T = int(input())
for test_case in range(1, T+1):
    CNT, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = 3

    ans = 0
    dfs(0, 0, 0)

    print(f'#{test_case} {ans}')