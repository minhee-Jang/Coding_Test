N, M = map(int, input().split())
water = []
for _ in range(N):
    water.append(list(map(int, input().split())))      #NxN index 0부터 주의
cloud = [[0 for _ in range(N)] for _ in range(N)]
move = []
for _ in range(M):
    d, s = map(int, input().split())
    move.append((d,s))

# 방향은 1부터 오니까
d8 = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)] #9개
# 4방향은 맘대로
d4 = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

init_c = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] #초기 구름 발생
for r, c in init_c:
    cloud[r][c] = 1 #구름 위치 표시

def move_cloud_rain(c, w, d, s):
    new_move = [[0 for _ in range(N)] for _ in range(N)]
    new_loc = []
    for i, j in c:
        ni, nj = (i + d8[d][0]*s)%N , (j + d8[d][1]*s)%N  #좌표 위치
        w[ni][nj] += 1
        new_move[ni][nj] = 1
        new_loc.append((ni, nj))
    # for row in new_move:
    #     print(*row)
    #
    # print("=====newmove=====")

    return new_move, new_loc, w

def copy_rain(c, w): # 물복사버그
    for i, j in c:
        count = 0
        for di, dj in d4:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:   #지금 격자 내
                if water[ni][nj] > 0: #물이 있으면
                    count +=1

        w[i][j] += count  #현재자리에 더해줌
    # for row in w:
    #     print(*row)
    #
    # print("==========")

    return w

def generate(curc, w): # 새로운 구름 생성
    genCloud = [[0 for _ in range(N)] for _ in range(N)]
    newCloud = []
    for i in range(N):
        for j in range(N):  #만약에 구름 값이 2보다 크면 구름 발생
            if curc[i][j] == 0 and w[i][j] >= 2: #2보다크고, 현재 구름 위치였던 곳이 아니라면
                water[i][j] -= 2 #물 소비
                genCloud[i][j] = 1 #새롭게 생성된 구름 위치
                newCloud.append((i,j))  # 구름 좌표

    return genCloud, newCloud, w

locCloud = init_c  #좌표위치
upWater = water  #물의 양 2차원

for d, s in move:
    curCloud, locCloud, upWater = move_cloud_rain(locCloud, upWater, d, s)
    upWater = copy_rain(locCloud, upWater)
    curCloud, locCloud, upWater = generate(curCloud, upWater)  #다음에 사용할 구름 위치 업데이트
    # for row in upWater:
    #     print(*row)
    # print("=======")

answer = 0
for i in range(N):
    for j in range(N):
        answer += upWater[i][j]
print(answer)