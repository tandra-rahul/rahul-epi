from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    # TODO - you fill in here.
    num = 0
    for i in range(len(col)):
        num += (ord(col[len(col)-i -1]) - ord('A') +1)*(26**i)

    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
