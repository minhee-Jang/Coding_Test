import sys

def bus(value):

    for k in range(1,N+1):    # 시간복잡도 100**3 
        for i in range(1, N+1):
            for j in range(1, N+1):
                value[i][j] = min(value[i][j], value[i][k] + value[k][j])

    return value


if __name__=="__main__":
    max_size = sys.maxsize
    N = int(input())
    B = int(input())

    value = [[max_size for j in range(N+1)] for i in range(N+1)]

    for i in range(1, N+1): # 출발 도착 같은건 0
        value[i][i] = 0
 
    for _ in range(B): # 시간복잡도 10만 
        a, b, c = map(int, input().split())
        if value[a][b] > c:
            value[a][b] = c
    
    value = bus(value)

    for i in range(1, N+1):   #시간복잡도 100**2 (max size는 제외)
        for j in range(1, N+1):
            if value[i][j] == max_size:
                value[i][j] = 0

        print(*value[i][1:])