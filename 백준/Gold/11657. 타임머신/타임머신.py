import sys 
def find():

    D[1] = 0  #출발 노드 1번

    for i in range(N-1): # 모든 노드 연결하는데 엣지 N-1개 필요
        for a, b, c in bus:
            if D[a]!=inf and D[b] > D[a] + c:
                # 출발이 무한대가 아니고, 가는 루트가 더 작을때
                D[b] = D[a] + c
    # 엣지 사이클 끝
    # 한 번 더 업데이트 되는 곳은 -1로  (음수 사이클)
    for a, b, c in bus:
        if D[a]!=inf and D[b] > D[a] + c:
            print(-1)
            sys.exit()
    for i in range(2, N+1):
        if D[i] == inf:
            print(-1)
        else:
            print(D[i])

    return


if __name__=="__main__":
    N, M = map(int, input().split())
    inf = sys.maxsize

    bus = []
    D = [(inf) for _ in range(N+1)]

    for i in range(M):
        a, b, c = map(int, input().split())
        bus.append((a, b, c))
    
    find()