import sys 
sys.setrecursionlimit(1000000)
def find(num, ans_list):
    if num in ans_list:
        return ans_list[num]   # 끊어주는 곳 -> 숫자가 있으면 return 으로 끊기 
    
    ans_list[num] = find(num-1, ans_list) + find(num-2, ans_list) + find(num-3, ans_list)  
    
    return ans_list[num]


if __name__=="__main__":
    input = sys.stdin.readline

    N = int(input())
    ans_list = {1: 1, 2:2, 3:4}

    for _ in range(N):
        num = int(input())
        if num> 3:
            ans = find(num, ans_list)
            print(ans)
        else:
            print(ans_list[num])