########## 얼음 녹일때 같은 격자에서 업데이트 하면 안됨 -> 동일한 시점에서 녹여야하니까 ic는 그대로 냅둬야함
########## 얼음 녹일때 음수 되는 애들 주의 안해서 틀림

from collections import deque
n, Q = map(int, input().split())
N = 2**n
ice = [[] for _ in range(N)]
for i in range(N):
    ice[i] = list(map(int, input().split()))
d = [(-1,0), (1, 0), (0, -1), (0, 1)]  #directions
L = list(map(int, input().split()))

def rotate(l, ic):
    l = 2**l# 격자 크기
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(0,N, l):
        for c in range(0, N, l):
            for ri in range(l):
                for ci in range(l):
                    temp[r + ri][c + ci] = ic[r + (l-1-ci)][c + ri]

    return temp

def melting(ic):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            count = 0
            for dr, dc in d:
                nr, nc = i + dr, j + dc
                if 0<=nr<N and 0<=nc<N: # 갈수있고
                    if ic[nr][nc] >0 : #얼음있으면
                        count +=1
            if count<=2: # 2개 이하면
                temp[i][j] = max(ic[i][j] - 1, 0)
            else:
                temp[i][j] = ic[i][j]


    return temp

def BFS(anic, i, j):  #N = 2**6 64*64*64
    global visited
    q = deque()
    q.append((i, j))

    visited[i][j] = True
    bigice = 1
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c  + dc
            if 0<=nr<N and 0<=nc<N:
                if visited[nr][nc] == False and anic[nr][nc]>0:  #갈수있고, 얼음있는 곳
                    bigice +=1
                    q.append((nr,nc))
                    visited[nr][nc] = True  #방문표시

    return bigice

answer_ice = ice
for i in range(Q):

    update_ice = rotate(L[i], answer_ice)
    answer_ice = melting(update_ice)

visited = [[False for _ in range(N)] for _ in range(N)]
answer = 0
ice_sum = 0 
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and answer_ice[i][j]>0: #다른곳에서 카운트 되지 않고, 얼음이 있다면 
            answer = max(BFS(answer_ice, i, j), answer)
        elif visited[i][j] == False and answer_ice[i][j]==0: #갈수는 있지만 얼음이 없는 곳
            visited[i][j] = True

        if answer_ice[i][j]>0: #얼음은 카운트
            ice_sum += answer_ice[i][j]

print(ice_sum)
if answer == 0:
    print(0)
else:
    print(answer)# 덩어리 구하기
