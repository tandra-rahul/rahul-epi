from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    lookup = {'(':')', '{':'}', '[':']'}
    leftchars = []

    for c in s:
        if c in lookup:
            leftchars.append(c)
        else:
            if len(leftchars) == 0:
                return False
            prev_char = leftchars.pop()
            if lookup[prev_char] != c:
                return False

    if len(leftchars) >0 :
        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
