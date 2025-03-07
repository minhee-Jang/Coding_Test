def solution(numbers, target):
    ans = 0
    def dfs(index, sum_num, ans):
    #재귀로 구현해보자 
    # 만약에 끝까지 도달했으면 -> 된다는거? 
        if index == len(numbers):
            if sum_num == target:
                ans +=1
            index = 0
            return ans # index 끝까지 확인했으면 돌아가기 
        # 더하는 경우
        # 빼는 경우
        ans = dfs(index+1, sum_num + numbers[index], ans) + dfs(index+1, sum_num - numbers[index], ans)
        return ans # 다음 스텝 구하기 

    return dfs(0, 0, ans)