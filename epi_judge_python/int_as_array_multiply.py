from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.

    if (num1 == [0]) or (num2 == [0]):
        return [0]

    # Take care of the sign
    si = int(num1[0]*num2[0]/(abs(num1[0])*abs(num2[0])))

    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    #M = [0]*(len(num1)*len(num2))

    for i in reversed(range(0, len(num1))):
        N = mult_digit(num2, num1[i])
        N += [0]*(len(num1) - i -1)
        if i == len(num1) -1:
            M = N
        else:
            M = add_lists(M, N)

    M[0] = si*M[0]
    return M

def add_lists(num1, num2):

    if len(num1) < len(num2):
        num1 = [0]*(len(num2) - len(num1)) + num1

    if len(num1) > len(num2):
        num2 = [0]*(len(num1) - len(num2)) + num2

    L = len(num1)
    S = [None]*L
    carry = 0

    for i in reversed(range(0, L)):
        N = num1[i] + num2[i] + carry
        S[i] = N % 10
        carry = int(N/10)

    if carry != 0:
        S.insert(0, carry)

    return S

def mult_digit(A,d):
    # Assume both positive
    M = [0]*(len(A))
    carry = 0
    for i in reversed(range(0, len(A))):
        N = A[i] *d + carry
        carry = int(N/10)
        M[i]  = N % 10

    if carry != 0:
        M.insert(0, carry)

    return M


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
