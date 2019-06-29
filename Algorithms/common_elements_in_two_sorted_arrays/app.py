def common_elements(given_array, given_array2):
    result = []
    p1 = 0
    p2 = 0

    while p1 < len(given_array) and p2 < len(given_array2):
        if given_array[p1] == given_array2[p2]:
            result.append(given_array[p1])
            p1 += 1
            p2 += 1
        elif given_array[p1] > given_array2[p2]:
            p2 += 1
        else:
            p1 += 1

    return result


def test():
    list_a1 = [1, 3, 4, 6, 7, 9]
    list_a2 = [1, 2, 4, 5, 9, 10]
    assert common_elements(list_a1, list_a2) == [1, 4, 9]

    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    assert common_elements(list_b1, list_b2) == [1, 2, 9, 10, 12]

    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    assert common_elements(list_c1, list_c2) == []


if __name__ == "__main__":
    test()
