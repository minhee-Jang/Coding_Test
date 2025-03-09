def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))               # string으로 바꾸어서 비교
    numbers.sort(key = lambda x : x*3,reverse=True)  # 3번씩 반복하면 붙였을때 큰수 찾기 가능
    #print(numbers)
    answer = answer.join(numbers)
    
    return str(int(answer))