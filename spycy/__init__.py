from inspect import getfullargspec
import types

__all__ = ['SpicyFunction']

class SpicyFunction:
    """
        Class that extends the functionality of basic functions to allow:
            * Composition
            * Currying
            * Application that avoids nesting

        Attributes:
            args: [\*ANY]
                List of arguments to be applied to the function.
            func: function
                Original function.
    """
    def __init__(self, func, **kwargs):
        argspec = getfullargspec(func)
        self._nargs = kwargs.pop('nargs', len(argspec.args))
        if self._nargs == 0:
            raise TypeError("Curried functions must have at least 1 argument")

        self.args = kwargs.pop('args', ())
        self.func = func
        self.__name__ = kwargs.pop('name', func.__name__)

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
        return '<spicy_function {}.{}>'.format(self.func.__module__, self.__name__)

    def __call__(self, *args):
        new_args = self.args + args # updating arguments
        arglen = len(new_args)

        if arglen > self._nargs:
            # Too many arguments provided!
            raise TypeError("{}() takes at most {} arguments ({} given)"
                                .format(self.func.func_name, self._nargs, arglen))

        if self._nargs == len(new_args):
            # With just the right amount of arguments, the function can be called.
            return self.func(*new_args)

        # Not enough arguments, keep saving them
        return SpicyFunction(self.func, args=new_args, nargs=self._nargs)


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
