import sys
import types
from collections.abc import Callable
from weakref import WeakKeyDictionary
from inspect import getfullargspec

_instances = WeakKeyDictionary()

class SpicyFunction(Callable):
    """
    Class that extends the functionality of basic functions to allow:
        * Composition
        * Currying
        * Application that avoids nesting

    This class should be called using the ``spice`` function rather than direct intantiation.

    Attributes:
        args: [\*ANY]
            List of arguments to be applied to the function.
        func: function
            Original function.
    """


    def init(self, func, nargs,args, name, doc):
        self.__wrapped__ = func;

        self._nargs = nargs or len(getfullargspec(func).args)
        if self._nargs == 0:
            raise TypeError("Curried functions must have at least 1 argument")

        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.__name__ = name or func.__name__
        if self.__name__ == '<lambda>':
            self.__name__ = '_lambda_'

        self.args = args or ()

    def __init__(self, func, nargs=None, args=None, name=None, doc=None):
        self.init(func, nargs, args, name, doc)


    def compose(self, other):
        """
        Built-in function to compose, i.e. use the result of ``self`` as input
        to another callable ``other``, preferably another SpicedFunction.

        :type other: callable
        :param other: Will receive the output of ``self`` when the resulting function is called.

        :returns: SpicedFunction -- The function composition `other(self(x))`
        """
        cfunc = lambda x: other(self(x))
        return SpicyFunction(cfunc, nargs=1, name='function_composition')

    def __repr__(self):
        return '<spicy_function {}.{}>'.format(self.__module__, self.__name__)

    def __call__(self, *arguments):
        new_args = self.args + arguments  # updating arguments
        arglen = len(new_args)

        if arglen > self._nargs:
            # Too many arguments provided!
            raise TypeError("{}() takes at most {} arguments ({} given)"
                                .format(self.__wrapped__.func_name, self.__nargs, arglen))

        if self._nargs == len(new_args):
            # With just the right amount of arguments, the function can be called.
            return self.__wrapped__(*new_args)

        # Not enough arguments, keep saving them
        return SpicyFunction(self.__wrapped__, args=new_args, nargs=self._nargs)


    """
    OPERATOR OVERLOAD
    =================
    """

    """
        Function composition
            f @ g (x) := f(g(x))
    """
    __matmul__ = compose

    """
        Alternative function application:
            f << x := f(x)
            x >> f := f(x)
    """
    __lshift__ = __rrshift__ = __call__

def spice(function, name=None, doc=None):
    if function not in _instances:
        _instances[function] = SpicyFunction(function, name=name, doc=doc)
    return _instances[function]
