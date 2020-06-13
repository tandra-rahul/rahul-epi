from test_framework import generic_test


def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    intermediate_results = []  # stack
    operators = {'+': lambda x,y: x+y, '-': lambda x,y: y - x,
                 '*': lambda x,y: x*y, '/': lambda x,y: y //x}
    delimiter = ','

    for item in expression.split(delimiter):
        if item in operators:
            intermediate_results.append(operators[item](intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(item))

    return intermediate_results[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
