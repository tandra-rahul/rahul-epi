from test_framework import generic_test
import math

def get_digit(x,i):

    return math.floor(x/10**(i-1))%10

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False

    if x >= 10:
        n = math.floor(math.log(x, 10)) + 1 # number of digits
        for i in range(1, math.floor(n/2) + 1):

            if get_digit(x, i) != get_digit(x, n-i+1):
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
