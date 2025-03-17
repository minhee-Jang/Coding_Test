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
