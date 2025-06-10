from collections import deque
from copy import deepcopy
D = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def is_inrange(r, c):
    return 0<=r<N and 0<=c<N

def FindGroup(game, ans):
    answer = 0
    flag = False
    M_visited = [[False for _ in range(N)] for _ in range(N)] # 무지개 블록은 갈 수 있음
    groups = [0, 0, 0, 0]
    groupsLoc = []
    for r in range(N):
        for c in range(N):
            if M_visited[r][c] or game[r][c] == -2:  # 간적 있는 block은 제외 / 빈칸은 제외
                continue
            else:
                # 탐색 가능
                b = game[r][c]
                if b > 0:
                    q = deque()
                    block = [1, 0, r, c]  # (넓이, 무지개 블록 수, r, c)
                    groupLoc = []
                    current = (r, c)
                    q.append((r, c))
                    groupLoc.append((r, c))
                    group_visited = [[False for _ in range(N)] for _ in range(N)]
                    M_visited[r][c] = True  # 일반 블록 탐색 완료 표시
                    group_visited[r][c] = True

                    while q:   
                        cr, cc = q.popleft()
                        for i in range(4):
                            nr, nc = cr + D[i][0], cc + D[i][1]
                            if is_inrange(nr, nc): # 격자 안
                                if not group_visited[nr][nc] and (b==game[nr][nc] or 0==game[nr][nc]):  # 방문하지 않은 곳, 같은 블럭이거나 무지개 블록
                                    groupLoc.append((nr, nc))
                                    q.append((nr, nc))
                                    block[0] += 1 # 넓이
                                    group_visited[nr][nc] = True
                                    if game[nr][nc] == 0: # 무지개
                                        block[1] += 1
                                    else:
                                        M_visited[nr][nc] = True  # 일반 블록인 경우 중복 탐색 방지
                                        # 기준 블록 설정
                                        if current > (nr, nc): # 그룹 안에서 가장 작은 기준 블록
                                            current = (nr, nc)
                                            block[2] = nr
                                            block[3] = nc
                                            
                    if block[0] >= 2: # 그룹 기준 완성, 최대 비교
                        flag = True
                        if groups < block:
                            groups = deepcopy(block)
                            groupsLoc = deepcopy(groupLoc)
                            answer = block[0] ** 2  # 점수 합산
    ans += answer
    return groupsLoc, ans, flag   # 지워질 위치

def gravity(game):
    for i in range(N-1, -1, -1):   # 밑에서부터 체크
        for j in range(N):
            r, c = i, j # 변수 받아
            if game[r][c] > -1:
                while True:
                    if is_inrange(r+1, c) and game[r+1][c] == -2:  # 계속 아래로 내리기
                        game[r+1][c] = game[r][c]
                        game[r][c] = -2
                        r += 1
                    else:
                        break
    return game

def rotate(game):
    newGame = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            newGame[N - 1 - j][i] = game[i][j]

    return newGame

def rearrange(game, loc): # game판, 없앨 블록

    for r, c in loc:
        game[r][c] = -2 # 빈칸

    game = gravity(game)
    game = rotate(game)
    game = gravity(game)

    return game

if __name__=="__main__":
    N, M = map(int, input().split())
    game = [ ]

    for _ in range(N):
        test = list(map(int, input().split()))
        game.append(test)

    ans = 0
    flag = True

    # AutoPlay
    while flag:
        loc, ans, flag = FindGroup(game, ans)
        game = rearrange(game, loc)

    print(ans)


        # Rearrange




