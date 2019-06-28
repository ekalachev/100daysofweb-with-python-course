def most_frequent(given_list):
    numbers = {}
    max_item = None
    max_count = 0

    for number in given_list:
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1

        if numbers[number] > max_count:
            max_item = number
            max_count = numbers[number]

    return max_item


def test():
    list1 = [1, 3, 1, 3, 2, 1]
    assert most_frequent(list1) == 1

    list2 = [3, 3, 1, 3, 2, 1]
    assert most_frequent(list2) == 3

    list3 = []
    assert most_frequent(list3) is None

    list4 = [0]
    assert most_frequent(list4) == 0

    list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
    assert most_frequent(list5) == -1


if __name__ == "__main__":
    test()
