from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    # TODO - you fill in here.
    # TODO - you fill in here.
    d = {}

    def num_ways_helper(top):

        if top == 0:
            return 1

        count = 0
        for i in reversed(range(1, maximum_step+1)):
            new = top - i
            if new >= 0:
                if new not in d:
                    d[new] = num_ways_helper(new)

                count += d[new]

        return count

    return num_ways_helper(top)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
