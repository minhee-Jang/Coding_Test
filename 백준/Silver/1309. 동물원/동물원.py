#DP
N = int(input()) 
#칸이 1 인경우
# 현재 칸 아예 안들어간 경우 1 / 있는 경우 2 / 총합 3
# dp = [1, 2, 3]
# a, b, count = dp
# for i in range(1, N):
#     b = a*2 + b
#     a = count
#     count = a + b

# print(count%9901)

# 머임 왜 메모리 이슈
# for i in range(1, len(dp)): 
#     dp[i][0] = dp[i-1][2] # 총합 그대로 내려옴
#     dp[i][1] = dp[i-1][0] * 2 + dp[i-1][1]  # 자리 지정
#     dp[i][2] = dp[i][0] + dp[i][1]  # 총합

dp = [[0] * 3 for _ in range(N)]
dp[0] = [1, 2, 3]
for i in range(1, N): 
    dp[i][0] = dp[i-1][2]%9901
    dp[i][1] = (dp[i-1][0] * 2 + dp[i-1][1])%9901
    dp[i][2] = (dp[i][0] + dp[i][1]) %9901
print(dp[N-1][2])








