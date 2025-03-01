N = int(input())

ans = [[] for _ in range(N+1)]

if N ==1 or N==2:
    print(1)
else:
    ans[1] = (0, 1)   # 0으로 끝나는거, 1로 끝나는거
    ans[2] = (1, 0)   # 0으로 끝나는거, 1로 끝나는거
    for i in range(3, N+1):
        a, b = ans[i-1]
        end_0 = a + b  # 0으로 끝나서 0을 붙인 수 + 1로 끝나서 0만 붙인 애들
        end_1 =  a    # 0로 끝나서 1만 붙인 애들
        ans[i] = (end_0, end_1)

    a, b = ans[N]
    print(a+b)
