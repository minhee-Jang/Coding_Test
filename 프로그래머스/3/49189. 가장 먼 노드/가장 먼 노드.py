import sys 
from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    node = [sys.maxsize for _ in range(n+1)]
    visted = [False for _ in range(n+1)]
    node[0] = 0
    node[1] = 0
    visted [1] = True
    myque = deque()
    myque.append(1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    while myque:
        cur = myque.popleft()
        for next in graph[cur]:  # 총 10만 쯤
            if visted[next] == False:
                if node[next] > node[cur] + 1:
                    node[next] = node[cur] + 1 
                myque.append(next)
                visted[next] = True   # 안가도 됨 
    
    max_value = max(node)
    answer = node.count(max_value)
    
    return answer