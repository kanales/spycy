import operator
from spycy.curry import curry



add = curry(lambda x,y: operator.add(x,y), name='add')
__add__ = curry(lambda x,y: operator.__add__(x,y), name='__add__')

and_ = curry(lambda x,y: operator.and_(x,y), name='and_')
__and__ = curry(lambda x,y: operator.__and__(x,y), name='__and__')

__contains__ = curry(lambda x,y: operator.__contains__(x,y), name='__contains__')
contains = curry(lambda x,y: operator.contains(x,y), name='contains')

concat = curry(lambda x,y: operator.concat(x,y), name='concat')

countOf = curry(lambda x,y: operator.countOf(x,y), name='countOf')

eq = curry(lambda x,y: operator.eq(x,y), name='eq')
__eq__ = curry(lambda x,y: operator.__eq__(x,y), name='__eq__')

floordiv = curry(lambda x,y: operator.floordiv(x,y), name='floordiv')
__floordiv__ = curry(lambda x,y: operator.__floordiv__(x,y), name='__floordiv__')

# reversed
ge = curry(lambda x,y: operator.ge(y,x), name='ge')
__ge__ = curry(lambda x,y: operator.__ge__(y,x), name='__ge__')

getitem = curry(lambda x,y: operator.getitem(x,y), name='getitem')
__getitem__ = curry(lambda x,y: operator.__getitem__(x,y), name='__getitem__')

# reversed
gt = curry(lambda x,y: operator.gt(y,x), name='gt')
__gt__ = curry(lambda x,y: operator.__gt__(y,x), name='__gt__')

indexOf = curry(lambda x,y: operator.indexOf(x,y), name='indexOf')
is_ = curry(lambda x,y: operator.is_(x,y), name='is_')
is_not = curry(lambda x,y: operator.is_not(x,y), name='is_not')

# reversed
le = curry(lambda x,y: operator.le(y,x), name='le')
__le__ = curry(lambda x,y: operator.__le__(y,x), name='__le__')

# reversed
lshift = curry(lambda x,y: operator.lshift(y,x), name='lshift')
__lshift__ = curry(lambda x,y: operator.__lshift__(y,x), name='__lshift__')

# reversed
lt = curry(lambda x,y: operator.lt(y,x), name='lt')
__lt__ = curry(lambda x,y: operator.__lt__(y,x), name='__lt__')

# reversed
matmul = curry(lambda x,y: operator.matmul(y,x), name='matmul')
__matmul__ = curry(lambda x,y: operator.__matmul__(y,x), name='__matmul__')

# reversed
mod = curry(lambda x,y: operator.mod(y,x), name='mod')
__mod__ = curry(lambda x,y: operator.__mod__(y,x), name='__mod__')

mul = curry(lambda x,y: operator.mul(x,y), name='mul')
__mul__ = curry(lambda x,y: operator.__mul__(x,y), name='__mul__')

ne = curry(lambda x,y: operator.ne(x,y), name='ne')
__ne__ = curry(lambda x,y: operator.__ne__(x,y), name='__ne__')

or_ = curry(lambda x,y: operator.or_(x,y), name='or_')
__or__ = curry(lambda x,y: operator.__or__(x,y), name='__or__')

pos = curry(lambda x,y: operator.pos(x,y), name='pos')

#reversed
pow = curry(lambda x,y: operator.pow(y,x), name='pow')
__pow__ = curry(lambda x,y: operator.__pow__(y,x), name='__pow__')

# reversed
rshift = curry(lambda x,y: operator.rshift(y,x), name='rshift')
__rshift__ = curry(lambda x,y: operator.__rshift__(y,x), name='__rshift__')

# reversed
sub = curry(lambda x,y: operator.sub(y,x), name='sub')
__sub__ = curry(lambda x,y: operator.__sub__(y,x), name='__sub__')

# reversed
truediv = curry(lambda x,y: operator.truediv(y,x), name='truediv')
__truediv__ = curry(lambda x,y: operator.__truediv__(y,x), name='__truediv__')

xor = curry(lambda x,y: operator.xor(x,y), name='xor')
__xor__ = curry(lambda x,y: operator.__xor__(x,y), name='__xor__')

#################################################

neg = curry(lambda x: operator.neg(x), name='neg')
__neg__ = curry(lambda x: operator.__neg__(x), name='__neg__')

not_ = curry(lambda x: operator.not_(x), name='not_')
__not__ = curry(lambda x: operator.__not__(x), name='__not__')

index = curry(lambda x: operator.index(x), name='index')
__index__ = curry(lambda x: operator.__index__(x), name='__index__')

itemgetter = curry(lambda x: operator.itemgetter(x), name='itemgetter')
methodcaller = curry(lambda x: operator.methodcaller(x), name='methodcaller')
attrgetter = curry(lambda x: operator.attrgetter(x), name='attrgetter')

truth = curry(lambda x: operator.truth(x), name='truth')
