def solution(k, tangerine):
    
    unique = list(set(tangerine))  # 1000만
    num = {i:0 for i in unique}

    for i in tangerine: # 10만 아래
        num[i] +=1     
    ans = []
    for i in unique:
        ans.append(num[i])
        
    ans = sorted(ans, reverse=True)
    
    current = 0
    i = 0
    while k > current:
        current += ans[i]
        i += 1
    return i