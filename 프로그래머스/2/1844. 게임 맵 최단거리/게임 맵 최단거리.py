from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    ans_map = [[-1 for _ in range(m)] for _ in range(n)] # 경로 누적 기록 
    ans_map[0][0] = 1
    direct = [(1,0), (0, 1), (-1, 0), (0, -1)]  
    myque = deque()
    myque.append((0,0))    # index = 0부터 주의
    
    while myque:
        x, y = myque.popleft()
        for xn, yn in direct:
            nex_x, nex_y = x + xn, y+yn
            if 0<=nex_x< n and 0<=nex_y< m:
                if ans_map[nex_x][nex_y] == -1 and maps[nex_x][nex_y] == 1:
                    myque.append((nex_x, nex_y))
                    ans_map[nex_x][nex_y] = ans_map[x][y] + 1        
    answer = ans_map[n-1][-1]
 
    return answer