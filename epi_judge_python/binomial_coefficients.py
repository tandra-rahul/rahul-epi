from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    # TODO - you fill in here.
    # if k == 0:
    #     return 1
    #
    # if k >= n//2:
    #     k = n - k
    #
    # result = 1
    # for i in range(1, k+1):
    #     result = (result * (n - i + 1))/i
    #
    # return result

    result = [0 if i >1 else 1 for i in range(k+1)]
    temp = [0]*(k+1)

    for i in range(1, n):
        #print(result)
        for j in range(k+1):
            temp[j] = result[j] + (result[j-1] if j >=1 else 0)

        result = temp[:]

    return result[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
