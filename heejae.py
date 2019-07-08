#월요일 오전실습

>>> def my_max(*args):
...     result = max([*args])
...     return result
...
>>> a = my_max(1,2,3)
>>> print(a)
3

>>> def my_max(*args):
...     result = 0
...     for i in args:
...             result = result.sort()
...             return result[-1]
...
>>> my_max(3,2,4,1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in my_max
AttributeError: 'int' object has no attribute 'sort'

>>> def my_min(*args):
...     result = min([*args])
...     return result
...
>>> b = my_min(1,2,3)
>>> print(b)
1

>>> def my_sum(*args):
...     result = 0
...     for i in args:
...             result = result + i
...     return result
...
>>> sum = my_sum(1,2,3,4,5,6,7,8,9,10)
>>> print(sum)
55

>>> def my_avg(*args):
...     result = 0
...     for i in args:
...             result += i
...     return result / len(args)
...
>>> my_avg(1,2)
1.5

#주말실습

>>> def my_join(str1, str2):
...     result = str1 + str2
...     return result
...
>>> my_join('My name is', ' Heejae')
'My name is Heejae'


>>> def my_split(str, ch):
...     result = str.split(ch)
...     return result
...
>>> my_split('I ate three apples yesterday',' ')
['I', 'ate', 'three', 'apples', 'yesterday']
