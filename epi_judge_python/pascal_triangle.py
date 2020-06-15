from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    result = []
    if n < 1:
        return result

    result.append([1])

    for i in range(1,n):
        #print(i, result)
        #print(len(result[0]))
        m = len(result[i-1])
        result.append([None]*(m+1))
        result[i][0] = result[i-1][0]
        result[i][m] = result[i-1][m-1]
        for k in range(1,m):
            result[i][k] = result[i-1][k-1] + result[i-1][k]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
