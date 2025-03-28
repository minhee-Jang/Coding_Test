
N, M = map(int, input().split())
r, c, d = map(int, input().split())
dir = {0: (-1, 0), 1:(0, 1), 2: (1, 0), 3:(0, -1)} #방향으로

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

def move_back(count, room, start_r, start_c, d):

    dr, dc = dir[d] #현재방향 

    if room[start_r - dr][start_c - dc] != 1: #후진방향 검사, 벽이 아니면 후진
        return start_clean(count, room, start_r - dr, start_c - dc, d)  #후진하고 방향 그대로
    else:
        print(count)
        exit()

def roate_find(count, room, r, c, d):

    for _ in range(4): 
        if d == 0:
            d=3
            dr, dc = dir[3]
        else:
            d -= 1
            dr, dc = dir[d]   # 반시계방향으로 탐색 

        if room[r + dr][c + dc] == 0: # 청소할 칸 있으면 (반시계방향으로 돌면서 탐색)
            room[r + dr][c + dc] = 2   # 청소c
            count +=1
            cur_dir = d  #  지금 방향 상태도 return
            return start_clean(count, room, r + dr, c + dc, cur_dir)
        
    return 

def start_clean(count, room, r, c, d):

    start_r, start_c = r, c
    if room[start_r][start_c] == 0: #현재위치 청소
        room[start_r][start_c] = 2
        count +=1
    roate_find(count, room, start_r, start_c, d)  # 찾고 

    move_back(count, room, start_r, start_c, d)


count = 0
start_clean(count, room, r, c, d)