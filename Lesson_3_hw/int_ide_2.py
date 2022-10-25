def no_of_times(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return no_of_times(n - 1) + no_of_times(n - 2)


if __name__ == '__main__':
    n = int(input('Stair no. '))
    print(f'Total ways to reach the {n}\'th stair are', no_of_times(n))