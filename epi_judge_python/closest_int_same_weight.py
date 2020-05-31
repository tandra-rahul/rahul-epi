from test_framework import generic_test


def swap_bits(x, i, j):

    if ( (x >>i)&1) != ( (x>>j) &1 ):
        return (x^ (2**i))^ (2**j)
    else:
        return x


def closest_int_same_bit_count(x: int) -> int:
    for i in range(0,63):
        if ( (x >>i & 1) != ( (x>>(i+1)) &1)):
            return swap_bits(x, i, i+1)
    return print("Error: invalid input")
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
