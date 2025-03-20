import sys

def main():
    n = int(input())
    mystack = []
    in_list = []

    data = sys.stdin.readline
    output = []

    for i in range(n):
        in_list = list(map(int, data().split()))

        if in_list[0] == 1:
            mystack.append(in_list[1])
        elif in_list[0] == 2:
            if mystack:
                output.append(mystack.pop())
                #print(mystack.pop())
            else:
                output.append('-1')
                #print(int(-1))
        elif in_list[0] == 3:
            #print(len(mystack))
            output.append(len(mystack))
        elif in_list[0] == 4:
            if mystack:
                output.append('0')
                #print(int(0))
            else:
                output.append('1')
                #print(int(1))
        elif in_list[0] == 5:
            if mystack:
                output.append(mystack[-1])
                #print(mystack[-1])
            else:
                output.append('-1')

    sys.stdout.write('\n'.join(map(str, output)) + '\n')


if __name__ == "__main__":
    main()


