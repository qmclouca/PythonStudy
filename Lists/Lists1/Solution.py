if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(0, N):
        user_input = input().split(' ')
        command = user_input.pop(0)
        if len(user_input) > 0:
            if 'insert' == command:
                eval("L.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
            else:
                eval("L.{0}({1})".format(command, user_input[0]))
        elif command == 'print':
            print (L)
        else:
            eval("L.{0}()".format(command))