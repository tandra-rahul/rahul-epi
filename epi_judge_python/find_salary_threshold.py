from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    # TODO - you fill in here.
    current_salaries.sort()
    salary_so_far = 0.0
    num_elements = len(current_salaries)

    for s in current_salaries:
        if s*num_elements >= target_payroll - salary_so_far:
            return (target_payroll - salary_so_far)/num_elements
        salary_so_far += s
        num_elements -= 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
