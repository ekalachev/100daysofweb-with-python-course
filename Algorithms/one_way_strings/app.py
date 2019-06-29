def is_one_away(s1, s2):
    min_length = min(len(s1), len(s2))
    max_length = max(len(s1), len(s2))
    if max_length - min_length > 1:
        return False

    dif_counter = 0
    index1 = 0
    index2 = 0
    while min_length > min(index1, index2):
        if s1[index1] == s2[index2]:
            index1 += 1
            index2 += 1
        else:
            dif_counter += 1
            if dif_counter > 1:
                return False
            if len(s1) > len(s2):
                index1 += 1
            elif len(s1) < len(s2):
                index2 += 1
            else:
                index1 += 1
                index2 += 1

    return True


def test():
    assert is_one_away("abcde", "abcd") is True
    assert is_one_away("abde", "abcde") is True
    assert is_one_away("a", "a") is True
    assert is_one_away("abcdef", "abqdef") is True
    assert is_one_away("abcdef", "abccef") is True
    assert is_one_away("abcdef", "abcde") is True
    assert is_one_away("aaa", "abc") is False
    assert is_one_away("abcde", "abc") is False
    assert is_one_away("abc", "abcde") is False
    assert is_one_away("abc", "bcc") is False


if __name__ == "__main__":
    test()
