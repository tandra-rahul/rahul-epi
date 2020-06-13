from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    if len(s) == 0:
        return True

    if len(s) == 0:
        return True

    s = s.lower()
    l, r = 0, len(s)-1

    while l <= r:
        #print(l, r)
        while not s[l].isalnum():
            l += 1
            if l >= len(s):
                return True

        while not s[r].isalnum():
            r -= 1
            if r <0:
                return True

        #print(l, r)
        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
