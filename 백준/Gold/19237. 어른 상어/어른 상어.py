N, M, K = map(int, input().split())

# N  = 20, M = N**2, K ==1000
# 상어는 번호가 클수록 강력함
# NxN -> 자신의 냄새를 뿌린다. 이후 상하좌우로 이동, K번 이동하면 냄새는 소멸
# 이동할 떄
# 1. 아무 냄새 없는 방향. 2. 자신의 냄새 있는 방향 -> 특정 우선순위 (방향따라 다름 셋팅 필요)
# 한칸에 여러마리 상어 -> 가장 작은번호 가진 상어 빼고 다 없애 

########### 전역변수 고려하지 못한거  #########
########### 상어 방향이랑 d 인덱스 헷갈린거거  #########

# aqau 정의 
aqua = []
for _ in range(N):
    aqua.append(list(map(int, input().split())))
# 상어 방향 정의 {} 1, 2, 3, 4 번 상어의 현재 방향 기록하기
 
ds = list(map(int, input().split())) # 인덱스 주의 0보다 큼큼
pri = [] 
for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    pri.append(temp)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 
# smell [상어번호, 냄새 카운트]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
 
# smell count 
# smell -1 씩 카운트 
def count_smell():
    for i in range(N):
        for j in range(N):
            #냄새 있음
            if smell[i][j][1]>0:
                smell[i][j][1] -= 1
            # 상어가 있음
            if aqua[i][j] != 0:
                smell[i][j] = [aqua[i][j], K]  # 상어 번호, 시작카운트
# move shark -> 
# 상어 이동 탐색 -> 이동 후 위치, 방향 
# 만약에 이동한 곳에 겹치는 애들 있으면 -> 탈락 
def move():   #N**2x8
    tmp = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if aqua[r][c] !=0: #상어
                curd = ds[aqua[r][c] -1]
                flag = False # 현재 상어 
                for idx in pri[aqua[r][c] -1][curd -1]:
                    nr, nc = r + d[idx-1][0] , c + d[idx-1][1]
                    if 0<=nr<N and 0<=nc<N: 
                        if smell[nr][nc][1] ==0:  #바로이동  
                            ds[aqua[r][c]-1] = idx
                            if tmp[nr][nc] == 0:
                                tmp[nr][nc] = aqua[r][c]
                            else: #냄새있음
                                tmp[nr][nc] = min(aqua[r][c], tmp[nr][nc])  # 작은놈 이김
                            flag = True #상어 이동완 ~
                            break
        
                if flag==False: #아직 상어 이동 못함
                    for idx in pri[aqua[r][c] -1][curd -1]:
                        nr, nc = r + d[idx-1][0] , c + d[idx-1][1]
                        if 0<=nr<N and 0<=nc<N: 
                            if smell[nr][nc][0] == aqua[r][c]: #자신의 냄새
                                ds[aqua[r][c]-1] = idx
                                tmp[nr][nc] = aqua[r][c]
                                break
    return tmp

answer = 0

while True:
    count_smell()           #N**2
    update = move()         #N**2x8
    answer +=1  
    aqua = update

    check = True
    for i in range(N):
        for j in range(N):
            if aqua[i][j] >1:  #다른 물고기 남아있으면 
                check = False
    if check:  #True면 끝내도 됨됨
        print(answer)
        break

    if answer>=1000: #1000초가 되어도 False
        print(-1)
        break





