import sys

def find(start, end):
    result = 0
    while end>=start:
        if start % 2 == 1: # 자식 노드 중 오른쪽 -> 독립적으로 사용
            result += list[start]
            start +=1
        if end % 2 ==0: # 자식 노드 중 왼쪽 -> 독립적으로 사용
            result += list[end]
            end -=1
        start = start //2
        end = end //2

    return result

def change(index, value):
    list[index] = value

    while index>1:
        index = index //2
        list[index] = list[index *2] + list[index * 2 + 1]
    #print(list)
    return

if __name__=="__main__":
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    k = 0
    while True:
        if 2**k >=N:
            break
        else:
            k+=1

    list = [0 for _ in range(2**(k+1))]
    for i in range(N):  # 배열 채우기
        num = int(input())
        list[i+2**k] = num

    for n in range(2**k -1 , 0, -1): # 7부터? 
        list[n] = list[2*n] + list[2*n+1]
    for _ in range(K+M):
        a, b, c = map(int, input().split())
        if a==1:
            index = b + 2**k -1 
            change(index, c)    
        else:
            if b !=c: 
                start = b + 2**k -1   # 질의 index로 바꿈
                end = c + 2**k -1
                print(find(start, end))
            else:
                end = c + 2**k -1
                print(list[end])