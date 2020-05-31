from test_framework import generic_test


def swap_bits(x, i, j):

    if ( (x >>i)&1) != ( (x>>j) &1 ):
        return (x^ (2**i))^ (2**j)
    else:
        return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
