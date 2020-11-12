from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # TODO - you fill in here
    n = len(individual_play_scores)
    count = [[0 for i in  range(final_score + 1)] for j in range(n)]

    # initialization
    for j in range(final_score + 1):
        if j % individual_play_scores[0] == 0 :
            count[0][j] = 1
        else:
            count[0][j] = 0

    for i in range(1,n):
        for j in range(final_score + 1):
            count[i][j] = count[i-1][j] + (count[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0)

    return count[n-1][final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
