from collections import deque
def solution(people, limit):
    people = sorted(people)  # NlogN   5만 * 4 = 20만?
    myque = deque(people)
    
    save = 0
    while myque:  # 다 구할 때까지
        remain = limit - myque.pop()  # 무조건 한명은 탈 수 있음 
        if myque:
            if remain >= myque[0]: # 제일 가벼운애 탈 수 있으면
                myque.popleft()
                
        save +=1
    return save