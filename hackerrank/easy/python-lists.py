if __name__ == "__main__":
    N = int(input())

    l = []
    for i in range(N):
        command, *args = input().split()
        args = list(map(int, args))
        if command == "insert":
            ix, val = args
            l.insert(ix, val)
        elif command == "print":
            print(l)
        elif command == "remove":
            l.remove(args[0])
        elif command == "append":
            l.append(args[0])
        elif command == "sort":
            l.sort()
        elif command == "pop":
            l.pop()
        elif command == "reverse":
            l.reverse()
