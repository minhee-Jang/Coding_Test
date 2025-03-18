from queue import PriorityQueue
def solution(operations):
    high = PriorityQueue()
    low = PriorityQueue()
    num_push = 0
    num_get = 0
    for com in operations:
        a, b = map(str, com.split(" "))
        if a == "I": 
            high.put((-int(b), int(b)))  # 내림차순으로
            low.put((int(b), int(b)))
            num_push+=1
        else:   # 하나남은 상태면 둘 다 뺴줘야하네
            if num_push == num_get:
                high = PriorityQueue()
                low = PriorityQueue()
            else:
                if int(b) == -1:
                    if not low.empty():
                        low.get()
                        # low.queue.remove((int(b), int(b)))
                else:#최대값 제거
                    if not high.empty():
                        high.get()
                num_get+=1
    ans = []
    h  = [] 
    for _ in range(len(high.queue)):
        _, value = high.get()
        h.append(value)
    l  = [] 
    for _ in range(len(low.queue)):
        _, value = low.get()
        l.append(value)

    for num in l:
        if num in h:
            ans.append(num)
            
    if not ans:
        answer = [0,0]
    else:   
        answer = [max(ans), min(ans)]

    return answer 
