from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))   #게임판


bli = []
for _ in range(M):
    d, s = map(int, input().split())
    bli.append((d, s))  #blizard

d4 = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # index 할 때 좌/하/우/상 순서
 # 토네이도 판 인덱싱
rS, cS = N//2, N//2
dirBli = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상  하 좌 우 순서

def tornado_index(r, c):
    index = []
    move = 0
    while True:
        for i in range(4): #4방향으로
            if i%2==0: #좌하/ 우상 짝으로 바뀌면
                move+=1
            for _ in range(move):
                #현재 방향 i
                nr, nc = r + d4[i][0], c + d4[i][1]
                index.append([nr, nc])
                r, c = nr, nc
                if nr ==0 and nc == 0:
                    return index    #토네이도 좌표 스택

def fill_blank(b):
    O = deque()
    newb = [[0 for i in range(N)] for j in range(N)]  #새로운 구슬 보드
    # 구슬 하나씩 꺼내고
    for r, c in index:
        if b[r][c] >0: #구슬 있으면
            O.append(b[r][c])  #구슬 넣어주고

    #구슬 다시 하나씩 넣어주기
    for r, c in index:
        if O:
            newb[r][c] = O.popleft()
        else:   #나머지는 이미 0
            break
    return newb

def throwICE(b, d, s):
    for i in range(1, s+1): #s안쪽은 다 없애야하니까
        r, c = rS + dirBli[d-1][0]*i, cS + dirBli[d-1][1]*i
        if 0<=r<N and 0<=c<N:#좌표내에 있으면 -> 사실 안해도 됨
            b[r][c] = 0

    return b


def bomb(b, result): # 구슬 폭발
    flag = False
    num, count = b[index[0][0]][index[0][1]], 1 #맨처음꺼 저장
    bl = [index[0]]
    #index 순서로 하나씩 빼서 검사
    for idx in range(1, len(index)):
        if num!= b[index[idx][0]][index[idx][1]]: #다른 구슬이면
            #구슬색이 다르지만 이미 count 4개 넘어감
            if num and count>=4:
                flag = True
                result[num-1] += count
                for r, c in bl:
                    b[r][c] = 0
            #구슬색이 다르고 , 4개 미만까지 온경우/ 혹은 앞에서 bomb 터지면 좌표 초기화, num은 현재 위치 가져옴
            bl = [index[idx]]
            num = b[index[idx][0]][index[idx][1]]  #다음색으로 체인지
            count = 1 # 초기화

        #같은 구슬일때는 bomb을 위해서, 다른 구슬일때는 새로운 시작을 위해 좌표 넣어줘야함
        else:
            bl.append(index[idx])
            count += 1  #횟수카운트 시작
    #마지막 구슬까지 확인했을때
    if num and count>=4: #마지막이 조건 맞는데 빠트린 경우가 되면 안되니까
        flag  = True
        result[num-1] += count
        for r, c in bl:
            b[r][c] = 0

    return flag, b, result # False 받을때까지 반복하게

def change(b):
    num, count = b[index[0][0]][index[0][1]], 1
    qc = deque()
    #구슬 색깔 바뀔때다 구슬 q에 분할해서 채워주기
    for idx in range(1, len(index)):
        if num != b[index[idx][0]][index[idx][1]]: #다음이랑 색 다르면
            if num!=0:
                qc.append(count)
                qc.append(num)   #구슬 변화
            num = b[index[idx][0]][index[idx][1]] #다음 색으로 교체
            count = 1
        else:
            count+=1
    if num: # 마지막 구슬이었다면
        qc.append(count)
        qc.append(num)

    #새로운 구슬 맵
    for r, c in index:
        if qc:
            b[r][c] = qc.popleft()
        else:
            b[r][c] = 0
    return b

index = tornado_index(rS, cS)   #상어좌표 기준 index #전역변수로 사용
answer = [0, 0, 0]
updateBoard = board
for i in range(M):
    d, s = bli[i]
    breaking = throwICE(updateBoard, d, s)  #얼음파편
    updateBoard = fill_blank(breaking)
    while True:
        f, updateBoard, answer = bomb(updateBoard, answer)
        if f == False:
            break # 더이상 폭발할 것 x
        else:
            updateBoard = fill_blank(updateBoard)

    updateBoard = change(updateBoard)
    #
    # for row in updateBoard:
    #     print(*row)
ans = 0
for i in range(1,4):
    ans += answer[i-1] * i
print(ans)
