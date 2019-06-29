def get_two_numbers_from_array_which_return_multiplication(given_array, multiplication):
    numbers = set()

    for number in given_array:
        quotient = multiplication / number

        if quotient in numbers:
            return quotient, number

        numbers.add(number)

    return None


def test():
    given_array = [2, 4, 1, 6, 5, 40, -1, 2]

    assert get_two_numbers_from_array_which_return_multiplication(given_array, 20) == (4, 5)
    assert get_two_numbers_from_array_which_return_multiplication(given_array, 40) == (1, 40)
    assert get_two_numbers_from_array_which_return_multiplication(given_array, 30) == (6, 5)
    assert get_two_numbers_from_array_which_return_multiplication(given_array, 11) is None


if __name__ == "__main__":
    test()
