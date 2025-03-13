def solution(s):
    s_list = list(map(str, s))

    mystack = []
    if s_list[0] == ')':
        return False
    
    for i in range(len(s_list)):
        if s_list[i] =="(":
            mystack.append(s_list[i])
        else:
            if mystack:
                mystack.pop()
            else:
                return False
    if mystack:
        return False
    else:
        return True