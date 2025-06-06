import sys
from collections import deque 
direct = [(0, 1), (1, 0), (-1, 0), (0, -1)] 

def findLoc(like, room): 

    loc_option = []
    maxLike = 0
 
    for r in range(N):        # 4*N**4   = 최대 10만
        for c in range(N):  
            if room[r][c] == 0:  # 사람 없으면 검사
                cnt = 0
                vacant = 0
                for i in range(4):
                    nr, nc = r + direct[i][0], c + direct[i][1]     
                    if (0<=nr<N and 0<=nc<N):   # 다음좌표 나가지 않을때, 인접한 카에서 비어있는 수랑, 좋아하는 학생 수 카운트
                        if room[nr][nc] ==0:
                            vacant +=1
                        elif room[nr][nc] in like[1:]:
                            cnt +=1
                
                new = (cnt, vacant, r, c)  # 새 option 
                if cnt>maxLike:   # 최대 갱신
                    loc_option = [new]
                    maxLike = cnt
                elif cnt == maxLike:
                    loc_option.append(new)
 
                #print(loc_option)
                 
    sorting = sorted(loc_option, key=lambda x:(-x[0], -x[1], x[2], x[3]))
    fr, fc = sorting[0][2], sorting[0][3]
    room[fr][fc] = like[0]
     
    return room

def satify(room, num):  # 만족도 조사

    sat = [[0 for _ in range(N)] for _ in range(N)]
    score = {0:0, 1:1, 2:10, 3:100, 4:1000}
    ans = 0
    sortingNum = sorted(num, key=lambda x:x[0])
    for r in range(N):               # N*N*4
        for c in range(N):
            cnt = 0
            friends = sortingNum[room[r][c]-1][1:]  #index 주의 - 친구 비교 리스트
 
            for i in range(4):
                    nr, nc = r + direct[i][0], c + direct[i][1]
                    if (0<=nr<N and 0<=nc<N):
                        if room[nr][nc] in friends:
                            cnt +=1
            ans += score[cnt]

    return ans

if __name__=="__main__":

    input = sys.stdin.readline
    N = int(input())
    num = []

    for _ in range(N*N):
        p, f1, f2, f3, f4 = map(int, input().split())
        num.append((p, f1, f2, f3, f4))   
 
    room = [[0 for _ in range(N)] for _ in range(N)]
       
    room[1][1] = num[0][0]   
    
    for i in range(1, N*N):  
        like = num[i]  #나랑 좋아하는 학생
        room = findLoc(like, room)
     
    # 걍 병렬로 
    print(satify(room, num))