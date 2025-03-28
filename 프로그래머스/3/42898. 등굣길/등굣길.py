from collections import deque

def solution(m, n, puddles):
    direction = [(0, 1), (1, 0)]
    map_pud = [[0 for i in range(m)] for i in range(n)]
    visited = [[False for i in range(m)] for i in range(n)]
    for i in range(len(puddles)):
        c, r = puddles[i]
        map_pud[r-1][c-1] = -1
        visited[r-1][c-1] = True
        
    map_pud[0][0] = 1
    #DP 탐색
    myque = deque()
    myque.append((0,0))

    while myque:
        cur_r, cur_c = myque.popleft()             # dp
        
        if (0<= cur_r<n and 0<= cur_c - 1<m) and map_pud[cur_r][cur_c - 1]!= -1:
            map_pud[cur_r][cur_c] += map_pud[cur_r][cur_c - 1]
        if (0<= cur_r-1<n and 0<= cur_c<m) and map_pud[cur_r-1][cur_c]!= - 1:   
            map_pud[cur_r][cur_c] += map_pud[cur_r - 1][cur_c]
            
        for (dr, dc) in direction:
            if 0<=(cur_r + dr) <n and 0<=(cur_c + dc) <m: 
                if visited[cur_r + dr][cur_c + dc] == False: #방문할 곳 추가
                    visited[cur_r + dr][cur_c + dc] = True
                    myque.append((cur_r + dr, cur_c + dc))
                     
    answer = map_pud[n-1][m-1] % 1000000007
    
    return answer