import sys 

def find_key(num, key):
    if len(key) == L:
        a_num = 0
        for i in a:  # 모음리스트
            if i in key:   #key 안에 모음이 있으면 count
                a_num +=1
        if 1<= a_num and a_num <= (L-2):  #모음이 적절하게 들어가있으면 
            for inte in key:
                print(chr(inte), end='')
            print()
        return
    
    for i in range(num+1, C):
        key.append(b[i]) 
        find_key(i, key)
        key.pop()

    return

if __name__=="__main__":
    input = sys.stdin.readline

    L, C = map(int, input().split())

    A = ['a', 'e', 'i', 'o', 'u'] #모음만 있는 리스트
    a = []
    b = list(map(str, input().split())) 
    
    for i in range(C):
        if b[i] in A:
            a.append(ord(b[i]))  
        b[i] = ord(b[i])
    a = sorted(a)
    b = sorted(b)
    #print(a, b)
    
    for i in range(C):
        key = [b[i]]
        find_key(i, key)