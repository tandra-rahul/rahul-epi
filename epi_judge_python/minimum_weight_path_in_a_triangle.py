from typing import List
import math

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    # TODO - you fill in here.
    # TODO - you fill in here.
    if len(triangle) == 0:
        return 0
    
    w = []
    for i in range(len(triangle)):
        w.append([0 for i in range(len(triangle[i]))])
        #print(i, w)
        for j in range(len(triangle[i])):
            #print(j)
            if i == 0:
                w[i][j] = triangle[i][j]
            else:
                term1 = math.inf if j == len(triangle[i])-1 else w[i-1][j]
                term2 = math.inf if j ==0 else w[i-1][j-1]
                w[i][j] = min(term1, term2) + triangle[i][j]

    min_weight = math.inf
    for i in range(len(w[-1])):
        min_weight = min(min_weight, w[-1][i])
    #print(w, min_weight)
    return min_weight


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
