def solution(phone_book):
    asc = sorted(phone_book) 
    for i in range(len(phone_book)-1): # 0 ~ N-2
        if asc[i] == asc[i+1][:len(asc[i])]: # 같으면
            return False
    return True

def error(phone_book):  #시간초과 ver
    asc = sorted(phone_book) 
    start = [{i:[] for i in range(0,10)} for j in range(0,21)] 
    for i in asc: #시작 수 filtering 
        s = str(i)[0] #시작수 
        l = len(str(i))
        start[l][int(s)].append(i) 

    answer = True
    for i in asc:   #  N 곱하기
        s = str(i)[0] #시작수   123 중 1
        l = len(str(i)) # 3
        for j in range(l+1, 21): # 해당 자리수부터   # 최대 20 곱하기
            if start[j][int(s)]: #요소 있으면 
                for k in start[j][int(s)]:
                    #print('serrch', i, 'key', k)
                    if str(i) == str(k)[:len(str(i))]:
                        answer = False
                        return answer

    return answer