from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    # TODO - you fill in here.
    current_salaries.sort()
    cumsum = 0.0
    num_elements = len(current_salaries)
    for salary in current_salaries:
        if cumsum + salary*num_elements < target_payroll:
            cumsum += salary
            num_elements -= 1
        else:
            return (target_payroll - cumsum)/num_elements

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
