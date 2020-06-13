from test_framework import generic_test


def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    if n == 1:
        return '1'

    init_seq = '1'
    num = 1

    while num < n:
        init_seq = generate_next(init_seq)
        num += 1

    return init_seq

def generate_next(s):
    result = []
    if len(s) == 1:
        result.append('1'+s)
        return ''.join(result)

    ind = 0;
    while ind < len(s):
        val, count = s[ind], 1
        while (ind +1) < len(s) and (s[ind] == s[ind+1]):
            ind += 1
            count+=1

        result.append(str(count) + val)
        ind +=1

    return ''.join(result)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
