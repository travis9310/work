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
>>> def my_max(*args):
...     result = 0
...     for i in args:
...             result = result.sort(i)
...     return result[-1]

>>> def my_max(*args):
...     result = args.sort()
...     return result[-1]

>>> def my_max(*args):
...     result = *args.sort()
...     return result[-1]


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
>>> my_sum(1,2,3,4,5)
15

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
