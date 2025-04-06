from collections import deque
def DFS(try_map, size, r, c):
    ans_opt=[]
    answer = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if try_map[i][j] < size and try_map[i][j] != 0: #사이즈보다 작으면 먹을 수 있어
                answer[i][j] = 100000000
            elif try_map[i][j] > size: #사이즈보다 크면 먹을 수 없고 지나갈 수 없음
                answer[i][j] = -1
    answer[r][c] = 0
    #print('before', answer)
    myque = deque()
    myque.append((r, c))  #상어 위치

    while myque:
        cur_r, cur_c = myque.popleft()
        for (dr, dc) in dir:
            if 0<=dr+cur_r<N and 0<=dc+cur_c<N:  # index 확인
                if answer[dr+cur_r][dc+cur_c] == 0: # 업데이트 전 + 지나갈 수 있음
                    if try_map[dr+cur_r][dc+cur_c] != 9:  #상어 위치가 아닐때
                        myque.append((dr+cur_r, dc+cur_c))
                        answer[dr+cur_r][dc+cur_c] = answer[cur_r][cur_c] + 1
                elif answer[dr+cur_r][dc+cur_c] == 100000000:  #먹이 가능한 도착지 앞
                    myque.append((dr + cur_r, dc + cur_c))
                    answer[dr +  cur_r][dc + cur_c] =answer[cur_r][cur_c] + 1
                    ans_opt.append((answer[dr + cur_r][dc + cur_c], dr + cur_r, dc + cur_c))   # 옵션 추가
    answer[r][c] = 0
    if ans_opt:
        ans_opt = sorted(ans_opt)
        return ans_opt[0]
    else:
        return 0, 0, 0

def main(aqua, init_r, init_c):
    #상어 크기 시작은 2
    size = 2
    count = 0
    eat = 0
    clear_r, clear_c = init_r, init_c
    aqua[init_r][init_c] = 0
    while True:
        if eat == size:
            eat = 0  # 먹이수 초기화
            size +=1  #사이즈업

        value, clear_r, clear_c = DFS(aqua, size, clear_r, clear_c)
        aqua[clear_r][clear_c] = 0  # clear

        if value == 0:   #엄마 도와줘 !!!!!!
            print(count)
            exit()
        else:

            count += value # 헤엄시간
            eat += 1   # 먹이감 빌드업

if __name__=="__main__":
    N = int(input())
    aqua = [[] for _ in range(N)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(N):
        aqua[i] = list(map(int, input().split()))
        for j in range(N):
            if aqua[i][j] == 9:
                s_r, s_c = i, j    # 아기상어 위치

    main(aqua, s_r, s_c)