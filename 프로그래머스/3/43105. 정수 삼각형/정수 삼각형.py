def solution(triangle):
    if len(triangle) ==1:
        return triangle[0][0]
    elif len(triangle) ==2:
        return max(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1])
    
    triangle[1] = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]
    
    for i in range(2, len(triangle)):
        before = triangle[i-1]  # 예전까지 합 
        for j in range(len(triangle[i])): #현재 배열
            if j ==0:
                triangle[i][j] = before[j] + triangle[i][j]
            elif j == len(triangle[i]) -1:
                triangle[i][j] = before[j-1] + triangle[i][j]
            else:
                triangle[i][j] = max(before[j], before[j-1]) + triangle[i][j]
    answer = max(triangle[-1])                  
    
    return answer