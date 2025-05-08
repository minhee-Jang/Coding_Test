def solution(number, k):  # stack 쌓고, 큰 수 오면 제거

    if k==len(number)-1:
        n = list(map(int, number)) 
        return str(max(n))
    else:
        ans = [] 
        for num in number: 
            while k>0 and ans and ans[-1]< num: 
                ans.pop()
                k -= 1
            ans.append(num) 
        answer = ''.join(i for i in ans)
        if k==0:  
            return answer
        else:    # k 아직 남으면  
            return answer[:len(number)-k]