if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command = input().split()
        name, args = command[0], map(int, command[1:])
        if name == "print": print(l); continue
        getattr(l, name).__call__(*args)