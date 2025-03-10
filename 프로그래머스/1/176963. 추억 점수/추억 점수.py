def solution(name, yearning, photo):
    answer = []
    # 모지 딕셔너리면 되자나
    ans = {}
    for i in range(len(name)):  # N = 100
        # 점수 리스트
        ans[name[i]] = yearning[i]
    # {"may:5 ~"}
    answer = []
    for pho in photo:   # 100 * 7
        remind = 0
        for peo in pho:
            if peo in name:
                remind += ans[peo]
        answer.append(remind)
    
    return answer