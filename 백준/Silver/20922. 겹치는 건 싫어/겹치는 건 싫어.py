import sys
from collections import deque
def find_max(que):
    max_len = 0

    for i in range(1, N+1):
        next_num = num_list[i]
        # print(que)
       #print(ans_find)
        if ans_find[next_num]==K:  # 최대 상태
            max_len = max(max_len, len(que))  # 최대 상태 업데이트트
            que.append(next_num) # 일단 넣고 
            ans_find[next_num]+=1
            while que:
                if que[0] == next_num:  # 똑같으면 pop 하고 
                    ans_find[que.popleft()]-=1
                    break
                else: 
                    ans_find[que.popleft()]-=1
        else:
            que.append(next_num)
            ans_find[next_num] +=1
            max_len = max(max_len, len(que))

    return max_len

if __name__=="__main__":
    input = sys.stdin.readline
    N, K = map(int, input().split())

    myque = deque()
    num_list = [0] + list(map(int, input().split())) # N + 1 개
    num_find = {i:0 for i in range(1,100001)}
    ans_find = {i:0 for i in range(1,100001)}
    find = False

    for i in range(1, N+1):  # 시간복잡도 N
        num_find[num_list[i]] +=1
        if num_find[num_list[i]]>K:
            find = True
            break
    
    if not find:
        print(N)
    elif N==K:
        print(N)
    else:
        print(find_max(myque))