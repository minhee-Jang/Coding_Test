import sys
N = int(input())

min_value = [0 for _ in range(N+1)]  

if N ==2 or N ==3:
    print(1)
    sys.exit()
elif N==1:
    print(0)
    sys.exit()

min_value[2] =1
min_value[3] =1

for i in range(4, N+1):
    if i % 3 ==0 and i % 2 == 0: # 둘다 나눠지면면
        min_value[i] = min(min_value[i//2] + 1, min_value[i//3] + 1, min_value[i-1] + 1)
    elif i % 3 ==0 and i % 2 != 0:
        min_value[i] = min(min_value[i//3] + 1, min_value[i-1] + 1)
    elif i % 3 !=0 and i % 2 == 0:
        min_value[i] = min(min_value[i//2] + 1, min_value[i-1] + 1)
    else:
        min_value[i] = min_value[i-1] + 1

#print(min_value)
print(min_value[N])