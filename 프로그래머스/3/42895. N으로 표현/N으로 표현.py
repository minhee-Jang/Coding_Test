def solution(N, number):
    if N==number:
        return 1
    opt = [list(set()) for _ in range(0,9)]  #8번사용까지 가능하니까
    for i in range(1,9):
        num = str(N)*i
        opt[i].append(int(num))  # 사용횟수칸에 N 넣어주고
    # 횟수 +1 때마다 사칙연산 -> 검사
    
    for i in range(2, 9):
        for j in range(1, i):
            poss = []
            for op1 in opt[j]:
                for op2 in opt[i-j]:
                    poss.append(op1+op2)
                    poss.append(op1*op2)
                    if op1!=0:
                        poss.append(op2//op1)
                    if op2!=0:
                        poss.append(op1//op2)
                    if op1 - op2>0:
                        poss.append(op1 - op2)
                    if op2 - op1>0:
                        poss.append(op2 - op1) 
            opt[i] += poss
        opt[i] = list(set(opt[i]))
        print(i, opt[i])
        if number in opt[i]: 
            return i
        
    return -1  #for 끝나면 없음