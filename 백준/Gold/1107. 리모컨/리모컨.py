#### 모범 답안
n = int(input())           # 목표 채널
m = int(input())           # 고장난 버튼 수
broken = set()

if m > 0:
    broken = set(map(int, input().split()))

# 숫자 버튼으로 특정 숫자를 누를 수 있는지 확인
def can_press(num):
    if num == 0:
        return 0 not in broken
    while num > 0:
        if num % 10 in broken:
            return False
        num //= 10
    return True

min_press = abs(n - 100)  # 초기값: + / - 버튼만 눌러서 이동하는 경우

for target in range(0, 1000000):  # 0 ~ 999999까지 전부 시도
    if can_press(target):
        press_count = len(str(target))  # 숫자 버튼 누른 횟수
        move_count = abs(n - target)    # 이동 횟수
        min_press = min(min_press, press_count + move_count)

print(min_press)


# import sys   #시간 오래걸린 버전
# from itertools import product  # 중복 순열 
# def find():
#     minclick = 500000  # 최대 오십만번 이동
#     minclick = min(minclick, abs(100 - N))  # 100번에서 시작
#     if len(poss) == 0: # 버튼 모두 고장
#         return minclick
#     elif len(poss) ==0: #고장난거 없으면
#         minclick = min(minclick, len(str(N)) + abs(N-test))
#     else:
#         # 가능한 경우의 수 만들면서 -> 최솟값 갱신
#         for i in range(len(str(N))-1, min(len(str(N))+2,6)): # 자릿수까지만 확인해도 되나 .. -> 틀렸음 +1 까지 해줘야함
#             if i ==0: 
#                 pass
#             else:
#                 for comb in product(poss, repeat=i): 
#                     #print(comb)
#                     test = int(''.join(map(str, comb)))
#                     testclick = len(str(test)) + abs(N-test)  # 버튼 누르는 수 + 채널 이동 수
#                     minclick = min(minclick, testclick)
#         return minclick

# if __name__=='__main__':
#     input = sys.stdin.readline

#     N = int(input())
#     outcnt = int(input())
#     num = list(map(int, input().split()))  # 고장난 숫자
    
#     poss = []
#     for i in range(10): # 0 ~ 9
#         if i not in num:   #10 x 10
#             poss.append(i)  #가능 다이얼

#     if N == 100:
#         print(0) 
#     else:
#         ans = find()
#         print(ans)
