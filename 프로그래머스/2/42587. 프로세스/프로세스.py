from collections import deque
def solution(priorities, location):
    #pri = N = 100 두번 돌아도 1000
    process = deque()
    for i in range(len(priorities)): #100
        process.append((priorities[i], i))   #(우선순위, index)
    
    run = 0
    while process: #1000
        pri, index = process[0] #첫번쨰꺼
        for i in range(len(priorities) - run):
            num, _ = process[i]
            if num > pri: #더큰거 있으면 
                process.append(process.popleft()) #뒤로
                break #for문 통과
            else:
                if i == (len(priorities) - run -1): #마지막
                    _, index = process.popleft()
                    run += 1
                    if index == location:
                        return run

