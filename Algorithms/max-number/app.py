import sys


def main():
    n = int(next(sys.stdin))

    arr_set = set()
    sum_of_indexes = 0
    index = 1

    while sum_of_indexes < n:
        sum_of_indexes += index
        arr_set.add(index)
        index += 1

    o = abs(n - sum_of_indexes)
    if o in arr_set:
        arr_set.remove(o)

    print(len(arr_set))
    print(*arr_set, sep=' ')


if __name__ == "__main__":
    main()
