def make_adder(n):
    """
    add(n, k) -> make_adder(n)(k)
    return a function that add input by n
    >>> add_3 = make_adder(3)
    >>> add_3(5)
    8
    """
    # def adder(k):
    #     return k + n
    # return adder
    # or use a lambda function
    return lambda k: k + n


def square(x):
    return x * x


def compose1(f, g):
    """
    >>> squader = compose1(square, make_adder(3))
    >>> squader(5)
    64
    >>> compose1(square, make_adder(3))(5)
    64
    """
    # def h(x):
    #     return f(g(x))
    # return h
    # or use a lambda function
    return lambda x: f(g(x))


def print_sums(x):
    """
    call `print_sums` on 1
    print 1
    def `next_sum` with x = 1
    return to `next_sum`

    call `next_sum` (with x = 1) on 3, i.e next_sum(1, 3)
    return to `print_sums` with 1 + 3

    call `print_sums` on 4
    print 4
    def `next_sum` with x = 4
    return to `next_sum`

    call `next_sum` (with x = 4) on 5, i.e next_sum(4, 5)
    return to `print_sums` with 4 + 5

    call `print_sums` on 9
    print 9
    def `next_sum` with x = 9
    return to `next_sum`

    call `next_sum` (with x = 9) on ?
    there are no more parameters, all procedures are over

    >>> print_sums(1)(3)(5)
    1
    4
    9
    """
    print(x)

    def next_sum(y):
        return print_sums(x + y)

    return next_sum

    # return lambda y: print_sums(x + y)


if __name__ == "__main__":
    print_sums(1)(3)(5)
    """
    1
    4
    9
    
    but doctest get 
    1
    4
    9
    <function print_sums.<locals>.next_sum at 0x000001F8A61A23E0>

    well... whatever
    """
