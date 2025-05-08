# 트럭 여러대 강 건너기 : 트럭이 최대 bridge_length 대 올라갈 수 있고, weight 이하로만 견딜 수 있음
# brideg_length/weight/truch_weight 는 10,000 이하 
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    i = 0
    q = deque()
    l = 0
    w = 0
    for tw in truck_weights:
    # queue로 앞으로 빼고 뒤로 넣고 - > 갯수 / 무게 계속 카운트 
        print(tw)
        while True:
            if l <= bridge_length -1 and w <= weight - tw: # 다리위에 공간 있고, 무게 버틸 수 있는 경우
                q.append(tw)  # 다리에 트럭 올리고
                print(q)
                l += 1
                w += tw 
                answer += 1 #그냥 올리는 경우도 ㄱㅊ지
                print('time', answer)
                break
            else: # 못올리는 경우  -> 공간이 없든 무게가 안되든 하나 빼야함 -> 계속 안되면 계속 빼야함 
                w -= q.popleft()  # 앞에꺼 나가고
                answer += bridge_length - l # 내보낼때까지 시간 카운트 lenght에 트럭에 k개 있으면 length - k -> 그리고 다시 while 문
                l -= 1 
                print('time', answer)
   
    if q: # 아직 차가 남아있으면 모두 다리를 건널 때 까지  
        answer += bridge_length
    print(answer)

    return answer