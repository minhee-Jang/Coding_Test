def tornado(s):
    start_r, start_c = N//2, N//2   #현재 토네이도 위치
    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]  #서쪽 남쪽 동쪽 북쪽
    i = 1
    count = 0
    d_num = 0
    away = 0
    while True:
        for _ in range(i):   #직진횟수
            nex_r, nex_c = start_r + dir[d_num][0], start_c + dir[d_num][1]  # 다음 토네이도 위치
            init_sand = s[nex_r][nex_c]  # 다음 토네이도 모래
            if init_sand !=0: #모래가 0이 아닐때만 계산
                move = 0
                for x, y, z in window[d_num]: #바람 리스트 불러와서 계산
                    t_r, t_c = nex_r + x, nex_c + y # 모래 좌표
                    if 0<=t_r<N and 0<=t_c<N: # 리스트 안에 있으면
                        fly = int(init_sand * z)
                        s[t_r][t_c] += fly  #현재모래에 날라온 모래 더하기
                        move += fly
                    else: #리스트 안에 없으면
                        fly = int(init_sand* z)
                        away += fly
                        move +=fly
                #퍼센트 모래 끝났으면 - 남은 모래는 a 자리에
                if 0<=nex_r + dir[d_num][0]<N and 0<=nex_c + dir[d_num][1]<N:
                    s[nex_r + dir[d_num][0]][nex_c + dir[d_num][1]] += (init_sand - move)
                else:
                    away += (init_sand - move)
                s[nex_r][nex_c] = 0
            if nex_r ==0 and nex_c ==0:

                return away
            start_r, start_c = nex_r, nex_c    #출발위치 변경
        count += 1
        d_num = (d_num + 1) % 4

        if count ==2:  #왼아래/ 오른위  2개마다 i증가
            i +=1   #토네이도 직진횟수 증가  while 문 안의 직진 수
            count = 0
        #while문마다 방향은 바꿔줘야함

if __name__ =="__main__":
    #서쪽으로
    left = [(-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),(-2, 0, 0.02),(1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02), (0, -2, 0.05)]
    #남쪽으로
    south = [(-y, x, z) for x, y, z in left]
    #동쪽으로
    right = [(x, -y, z) for x, y, z in left]
    #북쪽으로
    north = [(-x, y, z) for x, y, z in south]

    window = [left, south, right, north]

    N = int(input())
    sand = [[] for _ in range(N)]
    for i in range(N):
        sand[i] = list(map(int, input().split()))

    print(tornado(sand))