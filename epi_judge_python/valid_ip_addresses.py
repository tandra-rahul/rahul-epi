from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    # TODO - you fill in here.
    result = []
    for i in [1,2,3]:
        if is_valid_part(s[0:i]):
            for j in [1,2,3]:
                if is_valid_part(s[i: i +j]):
                    for k in [1,2,3]:
                        if is_valid_part(s[i+j: i+j+k]) and is_valid_part(s[i+j+k:]):
                            result.append(s[0:i] + '.' + s[i:i+j] + '.' + s[i+j: i+j+k] +'.'+s[i+j+k:] )
                #print(s[0:i], s[i:i+j], s[i+j: i+j+k], s[i+j+k:])
    return result

def is_valid_part(s):
    return s and (len(s)==1 or (s[0] != '0' and int(s) <= 255))

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
