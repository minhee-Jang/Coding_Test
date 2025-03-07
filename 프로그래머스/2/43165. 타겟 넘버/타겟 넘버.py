def solution(numbers, target):
    
    test = [0]
    s = []
    sum_num = 0
    for n in numbers:
        s = []   # 그전까지는 신경 x 마지막 합들만 고려 -> 2**20개 
        for _ in range(len(test)):
            current = test.pop()
            s.append(current + n)
            s.append(current + n*(-1))
        test = s      

    return s.count(target)