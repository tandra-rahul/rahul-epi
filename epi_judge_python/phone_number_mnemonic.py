from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    # TODO - you fill in here.
    d = {'0': '0', '1': '1', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
         '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}

    result = []
    if len(phone_number) == 0:
        return ['']

    for c in d[phone_number[0]]:
        result += [c+a for a in phone_mnemonic(phone_number[1:])]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
