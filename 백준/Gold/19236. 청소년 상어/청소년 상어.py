from copy import deepcopy

def DFS(r, c, s_dir, eat):
    global ans, board, fish, dir

    move_fish(r, c)  # 물고기 이동

    temp_board, temp_fish = deepcopy(board), deepcopy(fish)

    moved = False
    for step in range(1, 4):
        nr = r + dir[s_dir][0] * step
        nc = c + dir[s_dir][1] * step
        if not (0 <= nr < 4 and 0 <= nc < 4):
            break
        if not board[nr][nc]:  # 물고기 없음
            continue

        moved = True
        fish_num, next_dir = board[nr][nc]
        board[nr][nc] = []
        fish[fish_num] = []

        DFS(nr, nc, next_dir, eat + fish_num)

        board, fish = deepcopy(temp_board), deepcopy(temp_fish)

    if not moved:
        ans = max(ans, eat)

def move_fish(sr, sc):
    for i in range(1, 17):
        if fish[i]:
            fr, fc = fish[i]
            d = board[fr][fc][1]
            for j in range(8):
                nd = (d + j - 1) % 8 + 1
                nr = fr + dir[nd][0]
                nc = fc + dir[nd][1]
                if 0 <= nr < 4 and 0 <= nc < 4 and not (nr == sr and nc == sc):
                    board[fr][fc][1] = nd
                    if board[nr][nc]:
                        fish[board[nr][nc][0]] = [fr, fc]
                    board[nr][nc], board[fr][fc] = board[fr][fc], board[nr][nc]
                    fish[i] = [nr, nc]
                    break

if __name__ == "__main__":
    dir = [0, (-1, 0), (-1, -1), (0, -1), (1, -1),
           (1, 0), (1, 1), (0, 1), (-1, 1)]

    board = [[] for _ in range(4)]
    fish = [0 for _ in range(17)]
    for i in range(4):
        data = list(map(int, input().split()))
        for j in range(4):
            a, b = data[2 * j], data[2 * j + 1]
            board[i].append([a, b])
            fish[a] = [i, j]

    s_dir = board[0][0][1]
    eat = board[0][0][0]
    fish[eat] = []
    board[0][0] = []
    ans = 0
    DFS(0, 0, s_dir, eat)
    print(ans)
