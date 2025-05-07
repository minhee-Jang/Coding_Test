import sys
from collections import deque
# 입력
input = sys.stdin.readline
# visited 배열 저장 
C, R =  map(int, input().split()) #열, 행 순 입력
visited = [[False for _ in range(C)] for _ in range(R)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]   

flag = True # 첫 상태 검사
farm = []
q = deque()
cnt = 0
for r in range(R):   # 최악 - 백만
    ex = list(map(int, input().split()))
    farm.append(ex)  

    for c in range(C):
        if ex[c] == 0:  # 안익은 토마토 하나라도 있으면
            flag = False  # 다시 검사 x
            cnt += 1 # 안익은 토마토 세기
        elif ex[c] ==1 : # 익은 토마토
            q.append((r, c)) #시작 위치
            visited[r][c] = True

        else:
            visited[r][c] = True # -1 

if flag:
    print(0) # 저장될때부터 토마토 다 익은 상태   #option 1
    exit() 
else:
    maxday = 0
    while q: 
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc 
            if (0<=nr<R and 0<=nc<C) and (visited[nr][nc] == False and farm[nr][nc] == 0): #방문 가능,  안익은 상태
                farm[nr][nc] = farm[r][c] + 1
                maxday = max(maxday, farm[nr][nc])
                q.append((nr, nc))
                cnt -= 1

    if cnt == 0: #다익음
        print(maxday-1) #option 3
    else:
        print(-1)
     








