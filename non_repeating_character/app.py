def non_repeating(given_string):
    dictionary = {}

    for c in given_string:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

    for c in dictionary:
        if dictionary[c] == 1:
            return c

    return None


def test():
    assert non_repeating("abcab") == 'c'
    assert non_repeating("abab") is None
    assert non_repeating("aabbbc") == 'c'
    assert non_repeating("aabbdbc") == 'd'


if __name__ == "__main__":
    test()
