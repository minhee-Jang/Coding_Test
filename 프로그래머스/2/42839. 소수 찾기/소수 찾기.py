from itertools import permutations
from math import sqrt
def solution(numbers):  #N최대 5만
    if int(numbers) <=1:
        return 0
    if numbers in ["2", "3", "5", "7"]:
        return 1
    num = []
    for i in numbers:  # 7
        num.append(i)    
    num = sorted(num)
    all_num = []

    # 가능한 숫자 모두 만들기 -> 011 어케 처리?
    for i in range(1, len(numbers) + 1):   # 최대 5만
        nPr = permutations(num, i)
        for value in nPr:
            string = int(''.join(value))
            if len(str(string)) == i:    # permu 만들고 해당 자리수인거만 append     
                all_num.append(string)  
    # set - 중복 제거
    all_num = list(set(all_num)) # N+ NlogN

    max_value = max(all_num)
    
    for i in range(2, int(sqrt(max_value)+1)):  #logN
        for j in range(len(all_num)):
            if all_num[j]!=i and all_num[j] % i ==0:
                all_num[j] = 0
            elif all_num[j] <= 1:
                all_num[j] = 0
    print(all_num)
    print(len(all_num) - all_num.count(0))
    answer = len(all_num) - all_num.count(0)
        
    return answer