Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # TUPLE --> we can store different data types
>>> # duplicate values are allowed
>>> # indexig and slicing is possile
>>> # cant make any changes once tuple is created because its imutable
>>> t1 = (1,2,3,5,'hello','hey',5,767,-867,-33,0.88,66,4)
>>> t2 =(5,6.7,7,8,8,9,9,'python','programming',0.88,9.56)
>>> t3 = (66,77,88,99,33,22,22,11,'siva','krishna','class')
>>> print(t1,t2,t3)
(1, 2, 3, 5, 'hello', 'hey', 5, 767, -867, -33, 0.88, 66, 4) (5, 6.7, 7, 8, 8, 9, 9, 'python', 'programming', 0.88, 9.56) (66, 77, 88, 99, 33, 22, 22, 11, 'siva', 'krishna', 'class')
>>> len(t1)
13
>>> len(t2)
11
>>> len(t3)
11
>>> type(t1)
<class 'tuple'>
>>> t1[0]
1
>>> t2[7]
'python'
>>> t3[-3]
'siva'
>>> t1[0:7:1] #slicing
(1, 2, 3, 5, 'hello', 'hey', 5)
>>> t2[::2]
(5, 7, 8, 9, 'programming', 9.56)
>>> t3[-2:-8:1]
()
>>> t3[-2:9:1]
()
>>> t3[-2::]
('krishna', 'class')
>>> # adding elements
>>> t1[1] = 5
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t1[1] = 5
TypeError: 'tuple' object does not support item assignment
>>> # it is not possible to add elements once tuple is created since it is immutable
>>> # we can convert tuple into list and make changes
>>> t4 = list(t2)
>>> t4
[5, 6.7, 7, 8, 8, 9, 9, 'python', 'programming', 0.88, 9.56]
>>> type(t4)
<class 'list'>
>>> t5 = tuple(t4)
>>> type(t5)
<class 'tuple'>
>>> # joining two tuples
>>> t6 = t4+t5
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t6 = t4+t5
TypeError: can only concatenate list (not "tuple") to list
>>> t6 = t3+t5
>>> t6
(66, 77, 88, 99, 33, 22, 22, 11, 'siva', 'krishna', 'class', 5, 6.7, 7, 8, 8, 9, 9, 'python', 'programming', 0.88, 9.56)
>>> # count() --> how many times a particular element has been repeated
>>> t6.count(9)
2
>>> t6.count(77)
1
>>> t1
(1, 2, 3, 5, 'hello', 'hey', 5, 767, -867, -33, 0.88, 66, 4)
>>> (1,2,3,4) = t1
SyntaxError: cannot assign to literal
>>> t7 = ('cat','lion','sparrow')
>>> (pet, animal, bird) = t7
>>> print(pet)
cat
>>> print(animal)
lion
>>> print(bird)
sparrow
>>> # this process of assigning elements to the variables is called unpacking a tuple
>>> (pet, *living_beings) = t7
>>> print(pet)
cat
>>> print(living_beings)
['lion', 'sparrow']
>>> # when no. of variables are less than elements, we can add * to the variable
>>> t8 = t7*2
>>> print(t8)
('cat', 'lion', 'sparrow', 'cat', 'lion', 'sparrow')
>>> ('cat', 'lion', 'sparrow', 'cat', 'lion', 'sparrow')
('cat', 'lion', 'sparrow', 'cat', 'lion', 'sparrow')
>>> # multiply the tuple by 2
>>> 