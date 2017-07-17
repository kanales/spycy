import functools
import itertools
import operator
from spycy.curry import curry
# FUNCTIONS
def compose(*funcs):
    """
    Returns the function composition of two or more functions.

    Args:
        funcs ([function]): Each function should have exactly one argument.

    Returns:
        x |-> (f o g o ... o h)(x)

    """

    def fog(arg):
        for f in funcs:
            arg = f(arg)
        return arg
    return

def flip(func):
    @functools.wraps(func)
    def inner(*args):
        return func(*reversed(args))

    return inner


def pipe(*funcs):

    def pipe_(arg):
        # Compose is not used for efficiency reasons
        for f in funcs:
            arg = f(arg)
        return arg

    return pipe_

def negate(pred):
    def negated_predicate(x):
        return not pred(x)

    return negated_predicate

# UTILITIES

# predicates
def odd(x):
    return x&1

def even(x):
    return not odd(x)

def positive(x):
    return x > 0

def negative(x):
    return x < 0

# operations

# ITERATORS
filter_ = curry(lambda pred, it: filter(pred, it))

map_ = curry(lambda f, it: map(f,it))

reduce_ = curry(lambda f, it: functools.reduce(f, it))

def partition(pred, it):
    it1, it2 = tee(map(lambda x: (x,pred(x)), it))
    return ( (x for p,x in it1 if p)
           , (x for p,x in it2 if not p) )
partition_ = curry(partition)

def unpack(iterable, n):
    it = iter(iterable) # make sure it is an iterator
    return [next(it) for x in range(n)] + [it]

def head(iterable):
    it = iter(iterable)
    return next(it)

def tail(iterable):
    it = iter(iterable)

    try:
        while(1):
            prev = next(it)
    except StopIteration:
        pass

    return prev

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
