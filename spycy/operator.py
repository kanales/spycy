"""
This module contains all the functions from the ``operator`` module (bar some
functions that dind't feel like they belonged here) transformed into a
SpicyFunction so it can be used more confortable.

:Example:

Consider adding ``2`` to a list of numbers::

    map(add(2), [1,2,3,4,5])

"""

import operator
from spycy import SpicyFunction

__all__ = [ 'add', 'and_', 'contains', 'concat', 'countOf', 'eq', 'floordiv'
          , 'ge', 'getitem', 'gt', 'indexOf', 'is_', 'is_not', 'le', 'lshift'
          , 'lt', 'matmul', 'mod', 'mul', 'ne', 'or_', 'pos', 'pow', 'rshift'
          , 'sub', 'truediv', 'xor', 'neg', 'not_', 'index', 'itemgetter'
          , 'methodcaller', 'attrgetter', 'truth']

add = SpicyFunction(lambda x,y: operator.__add__(x,y), name='add', doc=operator.add.__doc__)
__add__ = SpicyFunction(lambda x,y: operator.__add__(x,y), name='__add__', doc=operator.add.__doc__)

and_ = SpicyFunction(lambda x,y: operator.and_(x,y), name='and_', doc=operator.and_.__doc__)
__and__ = SpicyFunction(lambda x,y: operator.__and__(x,y), name='__and__', doc=operator.and_.__doc__)

__contains__ = SpicyFunction(lambda x,y: operator.__contains__(x,y), name='__contains__', doc=operator.contains.__doc__)
contains = SpicyFunction(lambda x,y: operator.contains(x,y), name='contains', doc=operator.contains.__doc__)

concat = SpicyFunction(lambda x,y: operator.concat(x,y), name='concat', doc=operator.concat.__doc__)

countOf = SpicyFunction(lambda x,y: operator.countOf(x,y), name='countOf', doc=operator.countOf.__doc__)

eq = SpicyFunction(lambda x,y: operator.eq(x,y), name='eq', doc=operator.eq.__doc__)
__eq__ = SpicyFunction(lambda x,y: operator.__eq__(x,y), name='__eq__', doc=operator.eq.__doc__)

floordiv = SpicyFunction(lambda x,y: operator.floordiv(x,y), name='floordiv', doc=operator.floordiv.__doc__)
__floordiv__ = SpicyFunction(lambda x,y: operator.__floordiv__(x,y), name='__floordiv__', doc=operator.floordiv.__doc__)

# reversed
ge = SpicyFunction(lambda x,y: operator.ge(y,x), name='ge')
__ge__ = SpicyFunction(lambda x,y: operator.__ge__(y,x), name='__ge__')

getitem = SpicyFunction(lambda x,y: operator.getitem(x,y), name='getitem', doc=operator.getitem.__doc__)
__getitem__ = SpicyFunction(lambda x,y: operator.__getitem__(x,y), name='__getitem__', doc=operator.getitem.__doc__)

# reversed
gt = SpicyFunction(lambda x,y: operator.gt(y,x), name='gt')
__gt__ = SpicyFunction(lambda x,y: operator.__gt__(y,x))

indexOf = SpicyFunction(lambda x,y: operator.indexOf(x,y), name='indexOf', doc=operator.indexOf.__doc__)
is_ = SpicyFunction(lambda x,y: operator.is_(x,y), name='is_', doc=operator.is_.__doc__)
is_not = SpicyFunction(lambda x,y: operator.is_not(x,y), name='is_not', doc=operator.is_not.__doc__)

# reversed
le = SpicyFunction(lambda x,y: operator.le(y,x), name='le')
__le__ = SpicyFunction(lambda x,y: operator.__le__(y,x), name='__le__')

# reversed
lshift = SpicyFunction(lambda x,y: operator.lshift(y,x), name='lshift')
__lshift__ = SpicyFunction(lambda x,y: operator.__lshift__(y,x), name='__lshift__')

# reversed
lt = SpicyFunction(lambda x,y: operator.lt(y,x), name='lt')
__lt__ = SpicyFunction(lambda x,y: operator.__lt__(y,x), name='__lt__')

# reversed
matmul = SpicyFunction(lambda x,y: operator.matmul(y,x), name='matmul')
__matmul__ = SpicyFunction(lambda x,y: operator.__matmul__(y,x), name='__matmul__')

# reversed
mod = SpicyFunction(lambda x,y: operator.mod(y,x), name='mod')
__mod__ = SpicyFunction(lambda x,y: operator.__mod__(y,x), name='__mod__')

mul = SpicyFunction(lambda x,y: operator.mul(x,y), name='mul', doc=operator.mul.__doc__)
__mul__ = SpicyFunction(lambda x,y: operator.__mul__(x,y), name='__mul__', doc=operator.mul.__doc__)

ne = SpicyFunction(lambda x,y: operator.ne(x,y), name='ne', doc=operator.ne.__doc__)
__ne__ = SpicyFunction(lambda x,y: operator.__ne__(x,y), name='__ne__', doc=operator.ne.__doc__)

or_ = SpicyFunction(lambda x,y: operator.or_(x,y), name='or_', doc=operator.or_.__doc__)
__or__ = SpicyFunction(lambda x,y: operator.__or__(x,y), name='__or__', doc=operator.or_.__doc__)

pos = SpicyFunction(lambda x,y: operator.pos(x,y), name='pos', doc=operator.pos.__doc__)

#reversed
pow = SpicyFunction(lambda x,y: operator.pow(y,x), name='pow')
__pow__ = SpicyFunction(lambda x,y: operator.__pow__(y,x), name='__pow__')

# reversed
rshift = SpicyFunction(lambda x,y: operator.rshift(y,x), name='rshift')
__rshift__ = SpicyFunction(lambda x,y: operator.__rshift__(y,x), name='__rshift__')

# reversed
sub = SpicyFunction(lambda x,y: operator.sub(y,x), name='sub')
__sub__ = SpicyFunction(lambda x,y: operator.__sub__(y,x), name='__sub__')

# reversed
truediv = SpicyFunction(lambda x,y: operator.truediv(y,x), name='truediv')
__truediv__ = SpicyFunction(lambda x,y: operator.__truediv__(y,x), name='__truediv__')

xor = SpicyFunction(lambda x,y: operator.xor(x,y), name='xor', doc=operator.xor.__doc__)
__xor__ = SpicyFunction(lambda x,y: operator.__xor__(x,y), name='__xor__', doc=operator.xor.__doc__)

#################################################

neg = SpicyFunction(lambda x: operator.neg(x), name='neg', doc=operator.neg.__doc__)
__neg__ = SpicyFunction(lambda x: operator.__neg__(x), name='__neg__', doc=operator.neg.__doc__)

not_ = SpicyFunction(lambda x: operator.not_(x), name='not_', doc=operator.not_.__doc__)
__not__ = SpicyFunction(lambda x: operator.__not__(x), name='__not__', doc=operator.not_.__doc__)

index = SpicyFunction(lambda x: operator.index(x), name='index', doc=operator.index.__doc__)
__index__ = SpicyFunction(lambda x: operator.__index__(x), name='__index__', doc=operator.index.__doc__)

itemgetter = SpicyFunction(lambda x: operator.itemgetter(x), name='itemgetter', doc=operator.itemgetter.__doc__)
methodcaller = SpicyFunction(lambda x: operator.methodcaller(x), name='methodcaller', doc=operator.methodcaller.__doc__)
attrgetter = SpicyFunction(lambda x: operator.attrgetter(x), name='attrgetter', doc=operator.attrgetter.__doc__)

truth = SpicyFunction(lambda x: operator.truth(x), name='truth', doc=operator.truth.__doc__)
