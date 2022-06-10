"""CS 61A Discussion 01 Control and Environments"""

######################
# Chapter 2: Control #
######################

# 2.3
def count_digits(n):
    '''
    >>> count_digits(4)
    1
    >>> count_digits(12345678)
    8
    >>> count_digits(0)
    0
    '''
    ans = 0
    while n > 0:
        ans += 1
        n = n // 10
    return ans


# 2.4
def count_matches(n, m):
    '''
    >>> count_matches(10, 30)
    1
    >>> count_matches(12345, 23456)
    0
    >>> count_matches(121212, 123123)
    2
    >>> count_matches(111, 11) # only one's place matches
    2
    >>> count_matches(101, 10) # no place matches
    0
    '''
    ans = 0
    while n > 0 and m > 0:
        if n % 10 == m % 10:
            ans += 1
        n //= 10
        m //= 10
    return ans


#####################################
# Chapter 4: Higher Order Functions #
#####################################

# 4.5
def make_skipper(n):
    """
    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    def skip(m):
        for i in range(0, m + 1):
            if i % n:
                print(i)
    return skip


##############################
# Chapter 5: Extra Questions #
##############################

# 5.1
def ordered_digits(x):
    '''
    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    '''
    digit = 10
    while x:
        if x % 10 <= digit:
            digit = x % 10
        else:
            return False
        x //= 10
    return True


# 5.2
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def func(n):
        def calculate(x):
            circ = n // 3
            for i in range(0, circ):
                x = f3(f2(f1(x)))
            if n % 3 == 1:
                x = f1(x)
            elif n % 3 == 2:
                x = f2(f1(x))
            return x
        return calculate
    return func


# 5.3
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number is a palindrome.
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10 + y * 10
    while x > 0:
        x, y = x // 10, f()
    return y == n