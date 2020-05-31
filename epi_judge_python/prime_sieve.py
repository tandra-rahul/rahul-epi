from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.\
    A = [True]*(n+1)
    primes=[]

    for i in range(2,n+1):
        if A[i]:
            primes.append(i)
            for k in range(1, int(n/i)+1):
                A[k*i] = False

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
