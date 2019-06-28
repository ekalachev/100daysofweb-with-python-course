import heapq
from collections import Counter

def huffman_encode(s):



def main():
    s = input()

    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)

    print(len(code), len(encoded))

    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))

    print(encoded)


if __name__ == '__main__':
    main()
