from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    # TODO - you fill in here.
    count = [[0 for i in range(m)] for j in range(n)]

    for i in range(m):
        count[0][i] = 1

    for j in range(1, n):
        for i in range(m):
            count[j][i] = count[j-1][i] + ( count[j][i-1] if i >= 1 else 0)

    return count[n-1][m-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
