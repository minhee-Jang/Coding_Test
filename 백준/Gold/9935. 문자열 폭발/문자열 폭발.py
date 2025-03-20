import sys

string = str(input())
line = str(input())

len_s = len(string)    # 백만
len_l = len(line)      # 36
string_list = list(string)
# while 문자열 맨 마지막 index 까지
i = 0
ans = []
while i<len_s:
    ans.append(string_list[i]) 

    if len(ans)>= len_l and ''.join(ans[-len_l:]) == line:  #만약에 string이면 
        del ans[-len_l:]
    i += 1

if len(ans)>0:
    print(str(''.join(ans)))
else:
    print('FRULA')