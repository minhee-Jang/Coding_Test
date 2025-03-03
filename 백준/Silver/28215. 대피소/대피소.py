import sys
from itertools import combinations
if __name__=="__main__":
    input = sys.stdin.readline
    N, K = map(int, input().split())

    vil = []

    for _ in range(N):
        x, y = map(int, input().split())
        vil.append((x, y))

    # 마을 K개 조합 뽑고 -> 최솟값 구하기 
    comb = list(combinations(vil, K))
    ans = sys.maxsize

    # 시간복잡도 : 조합 50C2 * 마을 50 * 최대 k=3 
    for i in range(len(comb)):    # 조합하나씩    # 50C2 
        #print(comb[i])
        dist_k = []
        for x, y in vil:  # 마을 하나씩     # 50
            max_dis = sys.maxsize
            for a, b in comb[i]:   # 모든 대피소에서 집의 최소 거리 구하기
                dist = abs(x- a) + abs(y - b) # 거리 구하기

                max_dis = min(max_dis, dist)         # 집에서부터 세개의 대피소 중 가장 가까운 
            
            dist_k.append(max_dis)
        #print(dist_k)
        ans = min(ans, max(dist_k))
    print(ans)
             