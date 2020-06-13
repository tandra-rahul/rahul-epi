from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    # TODO - you fill in here.
    result = []
    ind = 0
    while ind < len(s):
        start = ind
        while ind < len(s) and s[ind].isnumeric():
            ind += 1

        #print(int(s[start:ind]))
        result.append(int(s[start:ind])*s[ind])
        ind += 1

    return ''.join(result)


def encoding(s: str) -> str:
    # TODO - you fill in here.
    result = []
    ind =0
    while ind < len(s):
        count = 1
        while (ind +1 < len(s)) and (s[ind] == s[ind+1]):
            count += 1
            ind += 1

        result.append(str(count)+s[ind])
        ind +=1

    return ''.join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
