def solution(n, costs):
    parent = [i for i in range(n)]
    
    for i in range(len(costs)):
        costs[i].reverse()
    asc_c = sorted(costs)
    print(asc_c) # 오름차순 -> 그리디
    
    def find(node):
        if parent[node] != node: #부모노드 있음
            parent[node] = find(parent[node])
        return parent[node]  #부모노드 재귀
    
    # 파인드 체크
    def union(n1, n2): 
        par_1 = find(n1)  # 4의 부모 3
        par_2 = find(n2)  # 6의 부모 2
        if par_1 != par_2: # 다르다면
            # 부모 통일 
            parent[par_1] = min(par_1, par_2)
            parent[par_2] = min(par_1, par_2)
            return True #answer 가능
        else: #같다면 -> 할필요 x
            return False
            

    #제일적은 가중치부터
    count = 0
    answer = 0
    for cost in asc_c:
        [co, n1, n2] = cost
        #만약 부모노드 다르다면 -> 작은거 대표노드로 만들어주고 answer 더하기
        if union(n1, n2):
            answer += co
            count +=1
        if count == n-1:
            return answer
        #부모노드 같다면 -> 할필요 없음 pass