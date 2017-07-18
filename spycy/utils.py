"""

"""

import functools
import itertools
import operator
from collections import deque
from spycy import spice

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

# TODO
#
#def flip(func):
#    """
#    Reverses the order of the arguments of a function.
#
#    :param func:
#        Function that will have its arguments reversed.
#    :type func:
#        function
#
#    :returns:
#        function -- This function is equivalent to the input function with
#        reversed arguments.
#    """
#    @spice
#    def inner(*args):
#        return func(*reversed(args))
#
#    return inner
#flip_ = spice(flip)


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
    @spice
    def negated_predicate(x):
        return not pred(x)

    return negated_predicate
negate_ = spice(negate)

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
odd_ = spice(odd)

def even(x):
    """
    See :func:`~spycy.utils.odd`
    """
    return not odd(x)
even_ = spice(even)

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
positive_ = spice(positive)

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
negative_ = spice(negative)

# operations

# ITERATORS
filter_ = spice(lambda pred, it: filter(pred, it), name='filter')

map_ = spice(lambda f, it: map(f,it), name='map')

reduce_ = spice(lambda f, it: functools.reduce(f, it), name='reduce')

def partition(pred, it):
    """
    Given a predicate, it splits an iterable into two iterators:
        * The truthy values
        * The falsy values

    :type pred:
        function: **A -> bool**
    :param pred:
        Predicate used to split the iterable.

    :type it:
        iterable (A)
    :param it:
        Iterable to be split.

    :returns:
        (A),(A) -- Iterators that split the iterable.
    """
    it1, it2 = tee(map(lambda x: (x,pred(x)), it))
    return ( (x for p,x in it1 if p)
           , (x for p,x in it2 if not p) )
partition_ = spice(partition)

def unpack(n, iterator):
    """
    Returns the n first elements of the iterator and then all the rest.
    Can be useful to unpack iterators without fully evaluating them.
    WARNING: this can modify the original iterator.

    :Example:
        ::
        it = iter([1,2,3,4])
        x, y, z = unpack(2, iter)
        # x, y are values; z is an iterator

    :type n:
        int
    :param n:
        Number of elements to be extracted from the iterator

    :type iterator:
        (A)

    :returns:
        A, A, ..., (A) -- n values and an iterator with the remaining elements.
    """
    # it = iter(iterable) # make sure it is an iterator
    return [next(it) for x in range(n)] + [it]
unpack_ = spice(unpack)

def head(iterable):
    """
    Gets the first element of the iterable.

    :param iterable:
        A non-empty iterable. If it is empty a StopIteration error will be raised
    :type x:
        iterable **(A)**

    :returns:
        A
    """
    it = iter(iterable)
    return next(it)
head_ = spice(head)

def tail(iterable):
    """
    Gets the last element of the iterable. WARNING: this consumes the iterable.

    :param iterable:
        A non-empty iterable. If it is empty a StopIteration error will be raised
    :type iterable:
        iterable **(A)**

    :returns:
        A
    """
    return deque(iterable, maxlen=1)[0] # using deque for C speed
tail_ = spice(tail)

def cons(x, iterator):
    """
    Can be used to insert an element x in the front of an iterator.

    :Example:
        ::
        it = iter([1,2])
        it = cons(0, it)
        next(it) # 0
        next(it) # 1
        next(it) # 2

    :type iterator:
        (A)

    :type x:
        A
    :param x:
        Value to be inserted to the front of the iterator

    :returns:
        (A)
    """
    yield x             # first comes x
    yield from iterator # then come all the other elements
cons_ = spice(cons)

def chain(*iterators):
    for it in iterators:
        yield from it


def n_wise(n, iterable):
    iters = itertools.tee(iterable, n)

    times = 0
    for it in iters:
        for x in range(times):
            next(it, None)

    return zip(iters)

def pairwise(iterable):
    return n_wise(iterable, 2)
