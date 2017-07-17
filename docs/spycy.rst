spycy package
=============

spycy module
---------------

.. automodule:: spycy
    :members:
    :undoc-members:
    :show-inheritance:

Submodules
----------

spycy.operator module
---------------------

.. automodule:: spycy.operator
    :members:
    :undoc-members:
    :show-inheritance:

spycy.utils module
------------------

.. automodule:: spycy.utils
    :members:
    :undoc-members:
    :show-inheritance:

.. function:: filter_(predicate, it)

	SpicyFunction representation of filter.

	:param predicate: Predicate function.
	:type predicate: function **A -> bool**

	:param it: Iterable collection
	:type it: iterable **(A)**
  
  	:return: **(A)**

.. function:: map_(predicate, it)

	SpicyFunction representation of map.

	:type predicate: function **A -> B**

	:param it: Iterable collection
	:type it: iterable **(A)**
  
  	:return: **(B)**

.. function:: reduce_(predicate, it)

	SpicyFunction representation of itertools.reduce.
	NOTE: This particular implementations always begins with 
	the first element of the iterable (this may change in the future).

	:param predicate: Reduction function
	:type predicate: function **(B,A) -> B**

	:param it: Iterable collection
	:type it: iterable **(A)**
  
  	:return: **B**
