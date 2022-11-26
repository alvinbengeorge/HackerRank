def print_formatted(number):
    spaceWidth = len(format(number, 'b'))
    for i in range(1, number+1):
        print(
            str(i).rjust(spaceWidth),
            format(i, 'o').rjust(spaceWidth),
            format(i, 'x').rjust(spaceWidth).upper(),
            format(i, 'b').rjust(spaceWidth)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)