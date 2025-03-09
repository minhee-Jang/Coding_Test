
def solution(n, times):
    # times = sorted(times)  # sorted 사용 NLogN
    max_time = n*max(times)  # 최대 N

    left = 1 
    right = max_time

    while left<=right:
        
        mid = (left + right)//2  # 몫 - 정수
        people = 0
        for i in times:
            if people>n : # 즁간에라도 사람 수 훨씬 초과하면 시간남음
                break
            people += (mid//i)   # 주어진 시간동안 볼 수 있는 사람 수
  

        if people>=n:  # 사람수 초과하면 시간 남음, 최적일 수 있으니 ans 저장
            answer = mid
            right = mid -1

        else:  # 사람 수가 훨씬 모자르면 -시간 부족함
            left = mid + 1

    return answer
    return answer