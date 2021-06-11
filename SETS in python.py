Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # SETS --> it can store different data types
>>> #duplicate values are not allowed
>>> # indexing and slicing also not possible
>>> #unordered and unindexed
>>> # it represents with {}
>>> a = {1,2,6,8,4,2,2,'movie','song'}
>>> print(a)
{'song', 1, 2, 4, 'movie', 6, 8}
>>> # sets cant have two items with same value, it appears in different order so no index or key
>>> print(a)
{'song', 1, 2, 4, 'movie', 6, 8}
>>> print(a)
{'song', 1, 2, 4, 'movie', 6, 8}
>>> b = {4,7,99,77,4,9,'hello','world'}
>>> c = {'hey','guys','hello'}
>>> len(b)
7
>>> d = {1,2,3.66,6.77,'krish','money',-55, True}
>>> type(d)
<class 'set'>
>>> # there is another method to create a set
>>> s1 = set(('fruits','veg','nonveg'))
>>> type(s1)
<class 'set'>
>>> # double braces are required
>>> # we can check a particular element is present in set
>>> print('fruits' in s1)
True
>>> print('veg' not in s1)
False
>>> print(a,b,c,d,s1)
{'song', 1, 2, 4, 'movie', 6, 8} {'hello', 99, 4, 'world', 7, 9, 77} {'hey', 'guys', 'hello'} {'money', 1, 2, 3.66, 6.77, -55, 'krish'} {'veg', 'fruits', 'nonveg'}
>>> # indexing and slicing is not allowed
>>> c[1:4]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c[1:4]
TypeError: 'set' object is not subscriptable
>>> #add() --> to add element in set
>>> s1.add('welcome')
>>> print(s1)
{'veg', 'fruits', 'welcome', 'nonveg'}
>>> c.add(4)
>>> print(c)
{'hey', 'guys', 4, 'hello'}
>>> #update() --> to add elements from one set to another set
>>> a.update(b)
>>> print(a)
{'song', 1, 2, 99, 4, 'movie', 6, 7, 8, 9, 77, 'world', 'hello'}
>>> list = [4,7,9,55,8.8,45,8.33]
>>> # we can add any data with the set by using update()
>>> c.update(list)
>>> print(c)
{4, 7, 8.8, 9, 8.33, 'guys', 45, 'hey', 55, 'hello'}
>>> e = d.copy()
>>> e
{'money', 1, 2, 3.66, 6.77, -55, 'krish'}
>>> # to remove an item in a set 1. remove(), 2.discard()
>>> c.remove('guys')
>>> c
{4, 7, 8.8, 9, 8.33, 45, 'hey', 55, 'hello'}
>>> # if once again we try to remove element'guys' it will give error
>>> c.remove('guys')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    c.remove('guys')
KeyError: 'guys'
>>> c.discard('hey')
>>> c
{4, 7, 8.8, 9, 8.33, 45, 55, 'hello'}
>>> # while trying with discard() i wont show error
>>> c.discard('hey')
>>> #pop() --> by using this method we can delete any random element, i will gives o/p as deleted element
>>> c.pop()
4
>>> c
{7, 8.8, 9, 8.33, 45, 55, 'hello'}
>>> c.pop()
7
>>> c
{8.8, 9, 8.33, 45, 55, 'hello'}
>>> #clear() --> it will empty the set
>>> c.clear()
>>> c
set()
>>> # del --> this will completely delette the set
>>> del c
>>> c
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> # union()
>>> # it will return with all elements from both sets
>>> s2 = 1.union(b)
SyntaxError: invalid syntax
>>> s2 = a.union(b)
>>> s2
{1, 2, 4, 'movie', 6, 7, 8, 9, 77, 'world', 'hello', 'song', 99}
>>> #intersection() --> gives the items that exists in both sets
>>> s3 = a.intersection(b)
>>> s3
{99, 4, 7, 9, 77, 'world', 'hello'}
>>> print(a,b)
{'song', 1, 2, 99, 4, 'movie', 6, 7, 8, 9, 77, 'world', 'hello'} {'hello', 99, 4, 'world', 7, 9, 77}
>>> s4 = s1.intersection(b)
>>> s4
set()
>>> s5 = a.difference(b)
>>> s5
{'song', 1, 2, 'movie', 6, 8}
>>> s6 = a.symmetric_difference(b)
>>> s6
{1, 2, 'movie', 6, 8, 'song'}
>>> s6 = s2.symmetric_difference(s5)
>>> s6
{99, 4, 7, 9, 77, 'world', 'hello'}
>>> print(s1,s2,s3,s4,s5,s6)
{'veg', 'fruits', 'welcome', 'nonveg'} {1, 2, 4, 'movie', 6, 7, 8, 9, 77, 'world', 'hello', 'song', 99} {99, 4, 7, 9, 77, 'world', 'hello'} set() {'song', 1, 2, 'movie', 6, 8} {99, 4, 7, 9, 77, 'world', 'hello'}
>>> print(a,b,d|)
SyntaxError: invalid syntax
>>> 
>>> print(a,b,d)
{'song', 1, 2, 99, 4, 'movie', 6, 7, 8, 9, 77, 'world', 'hello'} {'hello', 99, 4, 'world', 7, 9, 77} {'money', 1, 2, 3.66, 6.77, -55, 'krish'}
>>> 