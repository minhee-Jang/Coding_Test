import sys
from itertools import product  # 중복 순열
# 최대 숫자 50만 -> 6자리, 백만개 조합 가능
# def find():                                       #######시간초과
#     minclick = 500000  # 최대 오십만번 이동
#     minclick = min(minclick, abs(100 - N))  # 100번에서 시작
#     if len(poss) == 0: # 버튼 모두 고장
#         return minclick
#     else:
#         # 가능한 경우의 수 만들면서 -> 최솟값 갱신
#         for i in range(1, len(str(N))+2): # 자릿수까지만 확인해도 되나 .. -> 틀렸음 +1 까지 해줘야함
#             for comb in product(poss, repeat=i):
#                 test = int(''.join(map(str, comb)))
#                 testclick = len(str(test)) + abs(N-test)  # 버튼 누르는 수 + 채널 이동 수
#                 minclick = min(minclick, testclick)
#         return minclick
    
def find():
    minclick = 500000  # 최대 오십만번 이동
    minclick = min(minclick, abs(100 - N))  # 100번에서 시작
    if len(poss) == 0: # 버튼 모두 고장
        return minclick
    elif len(poss) ==0: #고장난거 없으면
        minclick = min(minclick, len(str(N)) + abs(N-test))
    else:
        # 가능한 경우의 수 만들면서 -> 최솟값 갱신
        for i in range(len(str(N))-1, min(len(str(N))+2,7)): # 자릿수까지만 확인해도 되나 .. -> 틀렸음 +1 까지 해줘야함
            if i ==0: 
                pass
            else:
                for comb in product(poss, repeat=i): 
                    #print(comb)
                    test = int(''.join(map(str, comb)))
                    testclick = len(str(test)) + abs(N-test)  # 버튼 누르는 수 + 채널 이동 수
                    minclick = min(minclick, testclick)
        return minclick

if __name__=='__main__':
    input = sys.stdin.readline

    N = int(input())
    outcnt = int(input())
    num = list(map(int, input().split()))  # 고장난 숫자
    
    poss = []
    for i in range(10): # 0 ~ 9
        if i not in num:   #10 x 10
            poss.append(i)  #가능 다이얼

    if N == 100:
        print(0) 
    else:
        ans = find()
        print(ans)
