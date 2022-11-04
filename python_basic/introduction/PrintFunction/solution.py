def print_function(n):
    print(*range(1, n + 1), sep="")


if __name__ == '__main__':
    n = int(input())
    print_function(n)
