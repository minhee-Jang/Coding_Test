import sys 
from collections import deque

def distance(value, des_r, des_c):        # 시간복잡도 N*M*4
    adds = [(0, 1), (-1, 0), (0, -1), (1, 0)]   
    for r, c in adds:                            # 첫번째에 대해 수행
        cur_r, cur_c = des_r + r, des_c + c
        if 0 < cur_r< N+1 and 0< cur_c < M+1 and value[cur_r][cur_c] == 1:
            myque.append((cur_r, cur_c))
            ans[cur_r][cur_c] = 1
            visited[cur_r][cur_c] = True

    while myque:  #BFS
        cur_r, cur_c = myque.popleft()
        for r, c in adds:
            nex_r, nex_c = cur_r + r, cur_c + c
            if 0 < nex_r< N+1 and 0< nex_c < M+1:
                # 업데이트 안한 곳이면/ 갈수있는 지역이면 
                if visited[nex_r][nex_c] == False and value[nex_r][nex_c] ==1:  
                    myque.append((nex_r, nex_c))
                    ans[nex_r][nex_c] = ans[cur_r][cur_c] + 1
                    visited[nex_r][nex_c] = True
    return ans

if __name__=="__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())

    visited = [[(False) for _ in range(M+1)] for _ in range(N+1)]
    ans = [[-1 for _ in range(M+1)] for _ in range(N+1)]
    value =[[0 for _ in range(M+1)]]
    myque = deque()

    for i in range(1, N+1):   # 시간목잡도 N * M
        arr = list(map(int, input().split()))
        arr = [0] + arr
        value.append(arr)
        for j in range(1, M+1):
            if arr[j] ==2:
                des_r, des_c = i, arr.index(2)
                visited[des_r][des_c] = True
                ans[des_r][des_c] = 0
            elif arr[j] == 0:
                ans[i][j] = 0

    ans = distance(value, des_r, des_c)
    for i in range(1, N+1):
        print(*ans[i][1:])