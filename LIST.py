Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [2,3,5.67,'siva',"python",-55,-8]
>>> b = [7,9,4,99,-67,'krish',"hello"]
>>> c = [1,2,3,4,5,6,7,8,9]
>>> print(a)
[2, 3, 5.67, 'siva', 'python', -55, -8]
>>> print(b)
[7, 9, 4, 99, -67, 'krish', 'hello']
>>> print(c)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(a,b)
[2, 3, 5.67, 'siva', 'python', -55, -8] [7, 9, 4, 99, -67, 'krish', 'hello']
>>> # in list, we can store in different data types
>>> #duplicate values are allowed and it is mutable
>>> type(a)
<class 'list'>
>>> type(a,b,c)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    type(a,b,c)
TypeError: type.__new__() argument 1 must be str, not list
>>> #indexing and slicling:
>>> a[0]
2
>>> b[4]
-67
>>> c[6]
7
>>> b[-1]
'hello'
>>> # to get  first three elements
>>> # to get  first three elements
>>> 
>>> a[0:3:1]
[2, 3, 5.67]
>>> a[:3]
[2, 3, 5.67]
>>> # slicing --> [start:stop:step]
>>> c[1:8:2]
[2, 4, 6, 8]
>>> # to get last five elements
>>> c[-5::]
[5, 6, 7, 8, 9]
>>> # to change values or elements in list
>>> c[3] = 41
>>> print(c)
[1, 2, 3, 41, 5, 6, 7, 8, 9]
>>> len[a]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    len[a]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(a)
7
>>> # insert
>>> # syntax --> (position/index, value)
>>> a.insert(3,'hello_world')
>>> print(a)
[2, 3, 5.67, 'hello_world', 'siva', 'python', -55, -8]
>>> b.insert(-2,6.888)
>>> print(b)
[7, 9, 4, 99, -67, 6.888, 'krish', 'hello']
>>> c.insert(-1,'hi')
>>> print(c)
[1, 2, 3, 41, 5, 6, 7, 8, 'hi', 9]
>>> a.insert(-0,4)
>>> print(a)
[4, 2, 3, 5.67, 'hello_world', 'siva', 'python', -55, -8]
>>> # append --> it will add element at the end of list
>>> a.append('fool')
>>> b.append(453)
>>> c.append('welcome')
>>> print(a,b,c)
[4, 2, 3, 5.67, 'hello_world', 'siva', 'python', -55, -8, 'fool'] [7, 9, 4, 99, -67, 6.888, 'krish', 'hello', 453] [1, 2, 3, 41, 5, 6, 7, 8, 'hi', 9, 'welcome']
>>> # extend --> it will add another list to current list
>>> a.extend(b)
>>> print(a)
[4, 2, 3, 5.67, 'hello_world', 'siva', 'python', -55, -8, 'fool', 7, 9, 4, 99, -67, 6.888, 'krish', 'hello', 453]
>>> print(b)
[7, 9, 4, 99, -67, 6.888, 'krish', 'hello', 453]
>>> # remove --> to remove a particular value in list
>>> a.remove('hello_world')
>>> print(a)
[4, 2, 3, 5.67, 'siva', 'python', -55, -8, 'fool', 7, 9, 4, 99, -67, 6.888, 'krish', 'hello', 453]
>>> #pop() --> it will remove any specific value by using index value, if we dont mention index it will remove last value
>>> a.pop()
453
>>> print(a)
[4, 2, 3, 5.67, 'siva', 'python', -55, -8, 'fool', 7, 9, 4, 99, -67, 6.888, 'krish', 'hello']
>>> a.pop(8)
'fool'
>>> a.pop(-1)
'hello'
>>> # del --> it can delete complete list or specific value
>>> del a[3]
>>> print(a)
[4, 2, 3, 'siva', 'python', -55, -8, 7, 9, 4, 99, -67, 6.888, 'krish']
>>> del b
>>> print(b)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined
>>> # clear --> it will remove content in list but list remain same
>>> c.clear()
>>> print(c)
[]
>>> # copying list using two methods --> 1. using assignment operator, 2. using .copy() function
>>> c = [4,7,9,54,'hai','hey','new',8.888]
>>> a = b
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a = b
NameError: name 'b' is not defined
>>> a = c
>>> print(a,c)
[4, 7, 9, 54, 'hai', 'hey', 'new', 8.888] [4, 7, 9, 54, 'hai', 'hey', 'new', 8.888]
>>> k = a
>>> print(k)
[4, 7, 9, 54, 'hai', 'hey', 'new', 8.888]
>>> a[3] = 'good'
>>> print(a,c,k)
[4, 7, 9, 'good', 'hai', 'hey', 'new', 8.888] [4, 7, 9, 'good', 'hai', 'hey', 'new', 8.888] [4, 7, 9, 'good', 'hai', 'hey', 'new', 8.888]
>>> # by changing one value in list 'a', remaining three lists also changes automatically
>>> #2. using .copy() function
>>> h = a.copy()
>>> print(h)
[4, 7, 9, 'good', 'hai', 'hey', 'new', 8.888]
>>> a[5] = 'software'
>>> print(a,h)
[4, 7, 9, 'good', 'hai', 'software', 'new', 8.888] [4, 7, 9, 'good', 'hai', 'hey', 'new', 8.888]
>>> # even after changing a value in list 'a' there is no change in list 'h'
>>> a,c,k,h
([4, 7, 9, 'good', 'hai', 'software', 'new', 8.888], [4, 7, 9, 'good', 'hai', 'software', 'new', 8.888], [4, 7, 9, 'good', 'hai', 'software', 'new', 8.888], [4, 7, 9, 'good', 'hai', 'hey', 'new', 8.888])
>>> 