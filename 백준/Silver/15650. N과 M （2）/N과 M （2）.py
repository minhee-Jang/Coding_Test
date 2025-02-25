from collections import deque
import sys 

def find(start):
    mystack.append(start)
    before_num = start
    current = start+1
    count = 1

    while mystack:
        if before_num< N and current <= N:
            if before_num < current and len(mystack) != M:
                mystack.append(current)
                current +=1
                before_num = mystack[-1]

            if current <= N:
                if len(mystack) == M:
                    print(*mystack)  # 1 2 3 10  
                    before_num = mystack.pop()   # 1 2 3 4
            else:
                print(*mystack)  # 1 2 3 10  
                #reset 
                # top = before_nu
                num_max = N
                while mystack and mystack[-1] == num_max:  # 스택이 있고, 스택 전 수가 자릿수의 max num이면 
                    mystack.pop()   
                    num_max -= 1
                if len(mystack) == 0: 
                    sys.exit()
                before_num = mystack.pop()  # 3   
                current = before_num + 1
                


    return

if __name__=="__main__":

    mystack = []
    N, M = map(int, input().split())

    num_list = [i for i in range(N+1)]   # index 0 부터
    # print(num_list)
    if M == 1:
        for i in range(1,N+1):
            print(i)
    else:
        for i in range(1, N-M+2): # 시작을 중심으로?
            find(i)