import sys 
from itertools import combinations
from collections import deque
import copy 
input = sys.stdin.readline

N, M = map(int, input().split())
lab = []
visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):   #O(N)
    row = list(map(int, input().split()))
    lab.append(row)

# 2, 0의 위치,
virus = []
no = []
for i in range(N):             # O(64)
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i, j))
            visited[i][j] = True
        elif lab[i][j] == 0:
            no.append((i, j))
        else:   #1 이어도 True
            visited[i][j] = True

nCr = combinations(no, 3)
answer = 0
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def BFS(vi, la):
    queue = deque()
    for (i, j) in virus:   #최대 10 
        # while
        queue.append((i, j))
        while queue:     #최대 64bb
            cur_i, cur_j = queue.popleft() 
            for (dr, dc) in d:
                nex_i, nex_j = cur_i + dr, cur_j + dc
                if 0<=nex_i<N and 0<=nex_j<M:  # 갈 수 있는 곳
                    if vi[nex_i][nex_j]==False:   # 가야하는 곳
                        la[nex_i][nex_j] = 2
                        vi[nex_i][nex_j] = True
                        queue.append((nex_i, nex_j))    #이동할 위치 추가

    count_0 = 0
    for i in range(N):   # 병렬로
        count_0 += la[i].count(0)
    #print(la)
    return count_0



for blind in nCr:   # 3개 벽  # 최대 5만    
    test_lab = [row[:] for row in lab]
    test_visited = [row[:] for row in visited]
    #print(visited[0], test_visited[0])


    test_lab[blind[0][0]][blind[0][1]] = 1
    test_lab[blind[1][0]][blind[1][1]] = 1
    test_lab[blind[2][0]][blind[2][1]] = 1
    

    test_visited[blind[0][0]][blind[0][1]] = True
    test_visited[blind[1][0]][blind[1][1]] = True
    test_visited[blind[2][0]][blind[2][1]] = True


    
    #print(test_visited)
    value = BFS(test_visited, test_lab)
    answer = max(answer, value)  # 최대값 업데이트 

print(answer)
 



