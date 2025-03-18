def solution(genres, plays):
    unique = {}
    all_g = []
    for i in range(len(genres)):
        if genres[i] not in unique:
            unique[genres[i]] = plays[i]
            all_g.append(genres[i])
        else:
            unique[genres[i]] = unique[genres[i]] + plays[i]
    
    # key값으로 정렬 unique = sorted(unique, reverse = True)
    # 역순으로 장르 뽑아서
    uni = []
    for gen in all_g:
        key, value = gen, unique[gen]
        uni.append((value, key))
    uni = sorted(uni, reverse = True)
    
    all_queue = []
    for _, genre in uni:  # 100 * 100000 = 십만
        music = []
        for i in range(len(genres)):
            if genre == genres[i]:
                music.append((plays[i], i)) 
        all_queue.append(sorted(music, reverse = True))
    ans = []
    for genre_list in all_queue:
        
        # 두개씩 넣기
        if len(genre_list) == 1:
            play_1, index_1 = genre_list[0]
            ans.append(index_1)
        else:
            
            play_1, index_1 = genre_list[0]
            play_2, index_2 = genre_list[1]
            
            if play_1 == play_2:
                ans.append(min(index_1, index_2))
                ans.append(max(index_1, index_2))
            else:
                ans.append(index_1)
                ans.append(index_2)
            
    return ans


def solution(genres, plays):
    answer = []
    
    d = {e:[] for e in set(genres)}   # genre유니크 값만 기록
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append((e[1], e[2]))  #각 장르에 play수랑 index
    genreSort = sorted(list(d.keys()), key = lambda x : sum(map(lambda y : y[0], d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key = lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp), 2)]  # 2개 이하면 하나만 
        
    return answer
    
    
    
    
