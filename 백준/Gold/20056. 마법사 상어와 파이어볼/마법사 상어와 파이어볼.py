def divide_fire():
    least1 = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):  ## 최악은 50X50X4
            if fire[i][j]:
                test = fire[i][j]
                num = len(test)

                if num == 1:
                    least1.append(test[0])  # 원소하나
                elif num > 1:
                    ms, ss, ds = 0, 0, 0
                    count, flag = 0, 0  # 0, 짝
                    for r, c, m, s, d in test:  # 방향 짝홀 추가
                        ms, ss, ds = ms + m, ss + s, ds + d  # sum 구하기
                        if d % 2 == 1:  # 홀이면
                            flag = 1
                        else:  # 짝
                            count += 1  # count == num, flag 0일 때 짝, count ==0, flag 1 일때 홀

                    if ms < 5:  # rule 2-1 초기화
                        fire[i][j] = []
                        #print("초기화")
                    else:  # rule 2-3 방향설정
                        fire[i][j] = []
                        if (count == num and flag == 0) or (count == 0 and flag == 1):  # 모두홀이거나짝이면
                            new_dir = [0, 2, 4, 6]
                        else:
                            new_dir = [1, 3, 5, 7]

                        new_m = ms // 5
                        new_s = ss // num
                        for new_d in new_dir:
                            fire[i][j].append((r, c, new_m, new_s, new_d))
                            least1.append((r, c, new_m, new_s, new_d))
    return least1

def inRange(x, y):
    if (0 < x <= N and 0 < y <= N):
        return x, y

    if x>N:
        while True:
            x -= N
            if x<=0:
                x+=N
                break
    elif x<=0:  #x=0일때 N으로
        while True:
            x+=N
            if x>0:
                break
            elif x==0:
                x = N
                break

    if y > N:
        while True:
            y -= N
            if y <= 0:
                y += N
                break
    elif y <= 0:  # x=0일때 N으로
        while True:
            y += N
            if y > 0:
                break
            elif y==0:
                y=N
                break

    return x, y


def move_fire(least1):
    global fire
    #print("before", fire)
    new_fire = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
    for r, c, m, s, d in least1:  # fire 업데이트     #최악 50X50x4
        nr, nc = r + fire_dir[d][0] * s, c + fire_dir[d][1] * s
        nr, nc = inRange(nr, nc)  # 좌표검사
        new_fire[nr][nc].append((nr, nc, m, s, d))

    fire = new_fire
    #print("after", fire)
    return least1


def main():
    global fire, least1

    for i in range(M):  # 파이어볼 개수만큼
        r, c, m, s, d = map(int, input().split())
        fire[r][c].append((r, c, m, s, d))
        least1.append((r, c, m, s, d))  # 파이어볼 있는 곳
    if M == 1:
        print(m)
        exit()

    for _ in range(K):
        least1 = move_fire(least1)
        least1 = divide_fire()

    ans = 0

    for r, c, m, _, _ in least1:
        ans += m

    print(ans)


if __name__ == "__main__":
    N, M, K = map(int, input().split())  # 파이어볼
    fire_dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 방향 설정
    fire = [[[] for _ in range(N + 1)] for _ in range(N + 1)]  # map 설정
    least1 = []

    if M == 0:
        print(0)
        exit()

    main()

