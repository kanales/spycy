"""

"""

import functools
import itertools
import operator
from collections import deque
from spycy import SpicyFunction

# FUNCTIONS
def pipe(*funcs):
    """
    Returns the function composition of two or more functions.

    :param funcs:
        All functions should have one argument, except the first function. Still,
        it is recommended for that function to have a single argument too.
    :type funcs:
        \*function

    :returns:
        function -- Evaluating the return function is equivalent to evaluating
        each function with the output of the preceding function.
    """
    def fog(arg):
        for f in funcs:
            arg = f(arg)
        return arg
    return

def flip(func):
    """
    Reverses the order of the arguments of a function.

    :param func:
        Function that will have its arguments reversed.
    :type func:
        function

    :returns:
        function -- This function is equivalent to the input function with
        reversed arguments.
    """
    @functools.wraps(func)
    def inner(*args):
        return func(*reversed(args))

    return inner

def negate(pred):
    """
    Given a predicate, returns a function that negates the output of the predicate;
    i.e. for every x, pred(x) = not negate(pred)(x)

    :param pred:
        Each function should have exactly one argument.
    :type pred:
        function: **\* -> bool**

    :returns:
        function -- Evaluating the return function is equivalent to evaluating
        each function with the output of the preceding function.
    """
    def negated_predicate(x):
        return not pred(x)

    return negated_predicate

# UTILITIES

# predicates
def odd(x):
    """
    :param x:
        Number to test.
    :type x:
        int

    :returns:
        bool -- True if x is odd False otherwise.
    """
    return x&1

def even(x):
    """
    See :func:`~spycy.utils.odd`
    """
    return not odd(x)

def positive(x):
    """
    :param x:
        Number to test.
    :type x:
        numeric

    :returns:
        bool -- True if x > 0 False otherwise.
    """
    return x > 0

def negative(x):
    """
    :param x:
        Number to test.
    :type x:
        numeric

    :returns:
        bool -- True if x < 0 False otherwise.
    """
    return x < 0

# operations

# ITERATORS
filter_ = SpicyFunction(lambda pred, it: filter(pred, it), name='filter')

map_ = SpicyFunction(lambda f, it: map(f,it), name='map')

reduce_ = SpicyFunction(lambda f, it: functools.reduce(f, it), name='reduce')

def partition(pred, it):
    it1, it2 = tee(map(lambda x: (x,pred(x)), it))
    return ( (x for p,x in it1 if p)
           , (x for p,x in it2 if not p) )
partition_ = SpicyFunction(partition)

def unpack(iterable, n):
    it = iter(iterable) # make sure it is an iterator
    return [next(it) for x in range(n)] + [it]

def head(iterable):
    """
    Gets the first element of the iterable.

    :param iterable:
        A non-empty iterable. If it is empty a StopIteration error will be raised
    :type x:
        iterable **(A)**

    :returns:
        **A**
    """
    it = iter(iterable)
    return next(it)
head = SpicyFunction(head)

def tail(iterable):
    """
    Gets the last element of the iterable. WARNING: this consumes the iterable.

    :param iterable:
        A non-empty iterable. If it is empty a StopIteration error will be raised
    :type x:
        iterable **(A)**

    :returns:
        **A**
    """
    return deque(iterable, maxlen=1)[0] # using deque for C speed
tail = SpicyFunction(tail)

def n_wise(iterable, n):
    iters = itertools.tee(iterable, n)

    times = 0
    for it in iters:
        for x in range(times):
            next(it, None)

    return zip(iters)

def pairwise(iterable):
    return n_wise(iterable, 2)

def cons(x, iterator):
    yield x             # first comes x
    yield from iterator # then come all the other elements

def chain(*iterators):
    for it in iterators:
        yield from it
