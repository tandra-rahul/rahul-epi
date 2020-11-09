from test_framework import generic_test


def square_root(k: int) -> int:
    # TODO - you fill in here.
    L, U, result = 0, k, 0
    while L <= U:
        mid = L + (U-L)//2
        if mid**2 > k:
            U = mid -1
        else:
            L = mid +1
            result = mid

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
