def solution(brown, yellow):
    #brown은 항상 짝수
    carpet = brown + yellow
    
    for i in range(brown):
        n = i
        m = (brown - 2*n +4)/2
        
        if n*m == carpet:   
            return [max(n,m), min(n,m)]
            
    return answer