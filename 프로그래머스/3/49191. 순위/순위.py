# 순위 결정되려면 모든 선수와 다 겨뤄봐야 함 -> 만약에 가는 루트 있으면 반대는 진다는 소리
### 플로이드 와샬ㅋ
# 순위 - 자신 제외한 모든 인원과 승패가 확정되어 있어야함
def solution(n, results):
    answer = 0
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    for a, b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1, -1]: #같거나 이미 아는 경우는
                    continue
                if board[i][k] == 1 and board[k][j] == 1:
                    # 만약에 간접적으로 승리 유추 가능
                    board[i][j] = 1
                    board[j][i] = -1 
                    board[j][k] = -1
                    board[k][i] = -1  # 반대로가는 루트는 모두 패
                    
    # 자신 제외하고 승패 아는지 확인
    ans = [0 for _ in range(n)]
    me = []
    s = 0
    for i in range(n):
        s += board[i].count(1)
        me.append(s) 
        s= 0
        for j in range(n):
            if board[j][i] ==1:
                ans[i] += board[j][i] # 0-0 1-0 2-0
    
    for i in range(n):
        if ans[i] + me[i] == n -1:
            answer += 1 
    
    return answer