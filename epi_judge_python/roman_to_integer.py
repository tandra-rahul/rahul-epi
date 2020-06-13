from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    # TODO - you fill in here.
    result = 0
    ind = 0
    dict ={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV': 4, 'IX':9, 'XL': 40, 'XC':90, 'CD':400, 'CM':900}
    while ind < len(s):

        if ind == len(s) -1:
            result += dict[s[ind]]
        elif s[ind: ind+2] in dict:
            result += dict[s[ind:ind+2]]
            ind += 1
        else:
            result += dict[s[ind]]

        ind +=1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
