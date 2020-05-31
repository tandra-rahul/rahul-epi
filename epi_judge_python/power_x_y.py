from test_framework import generic_test


def power(x: float, y: int) -> float:

    if y == 0:
        return 1

    if y & 1 :
        z = pow(x, (y-1)/2)
        return x*z*z
    else:
        z = pow(x, y/2)
        return z*z




if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
